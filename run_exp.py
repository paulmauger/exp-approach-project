from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_j, K_f
import random
from constants import *
from exp_utils import *
from trial import *
import argparse

""" Global Settings """

#==================================================================
# Parse Command Line Arguments
#==================================================================

parser = argparse.ArgumentParser(description="Run the fast-syntax experiment.")
parser.add_argument('--id', type=int, default=1)
parser.add_argument('--mode', type=str, default='full', choices=['full', 'train', 'experiment'])
args, extras = parser.parse_known_args()

participant_ID = args.id
mode = args.mode
flags = set(extras)

#==================================================================
# Experiment Setup
#==================================================================

exp = design.Experiment(name="Stroop", background_colour=C_WHITE, foreground_colour=C_BLACK)
exp.add_data_variable_names(['block_cnt', 'trial_cnt', 'trial_type', 'word', 'color', 'RT', 'correct'])

if '--fullscreen' not in flags:
    control.set_develop_mode()
    scale_factor = 1.0
else: 
    #In fullscreen, the elements seem smaller than in develop mode, so we scale them up
    scale_factor = 1.8

control.initialize(exp)

""" Stimuli """

#Scale stimuli differently if fullscreen or not (develop mode)
fixation = stimuli.FixCross(size=(int(20 * scale_factor), int(20 * scale_factor)), line_width=int(3 * scale_factor))
hashmask = stimuli.TextLine("#################", text_size=int(22 * scale_factor))
stim_text_size = int(22 * scale_factor)
feedback_correct = stimuli.Circle(radius=int(10 * scale_factor), colour=C_GREEN)
feedback_incorrect = stimuli.Circle(radius=int(10 * scale_factor), colour=C_RED)
bar_y_offset = int(40 * scale_factor)
bar_size = (int(2 * scale_factor), int(30 * scale_factor))
bar_top = stimuli.Rectangle(size=bar_size, position=(0, bar_y_offset), colour=C_BLACK)
bar_bottom = stimuli.Rectangle(size=bar_size, position=(0, -bar_y_offset), colour=C_BLACK)
bars = [bar_top, bar_bottom]


load([fixation, hashmask, feedback_correct, feedback_incorrect, bar_top, bar_bottom])

#Counterbalance lists List A and List B between participants
#List_A and List_B are the counterbalanced lists such as, for each row of the original CSV, 
#if List_A contains the normal version then List_B contains the scrambled version or vice versa.
#those lists are generated in counterbalancing.py

if participant_ID % 2 == 0:
    seqs_list = load_csv('tables/List_A.csv')
else:
    seqs_list = load_csv('tables/List_B.csv')


#========================================================================
# Pseudo-randomly shuffle the order of the the lists for each participant
#========================================================================

seqs_list = shuffle_list(seqs_list, max_repetitions=3)  #exp_utils.py

#========================================================
#Counterbalance key pairs to answer between participants 
#========================================================

if participant_ID % 4 < 2:
    INSTR_START = INSTR_START_J_CORRECT
    INSTR_TRAINING = INSTR_TRAINING_J_CORRECT
    j_is_correct = True
else:
    INSTR_START = INSTR_START_F_CORRECT
    INSTR_TRAINING = INSTR_TRAINING_F_CORRECT
    j_is_correct = False


control.start(subject_id=participant_ID)

#================================================
# Training trials if applicable in this execution
#================================================

#If the mode is 'full' or 'train', we run the training block.
if mode in ['full', 'train']:
    present_instructions(exp, INSTR_TRAINING, scale_factor)

    seqs_trial = load_csv('tables/List_Training.csv')
    print(seqs_trial)
    for trial_id in range(1, NB_TRIALS_TRAINING + 1):
        sequence = seqs_trial[trial_id-1]
        run_trial(exp, "TRAINING", trial_id, sequence['cond'], sequence['text'], j_is_correct, fixation, hashmask, feedback_correct, feedback_incorrect, stim_text_size, bars)
    
    #If we only asked for the training part, end the execution here.
    if mode == 'train':
        present_instructions(exp, INSTR_END, scale_factor)
        control.end()
    
    #Otherwise, display the instructions and continue to the experiment
    present_instructions(exp, INSTR_END_TRAINING, scale_factor)

#==================================================================
# Loop for blocks and trials: NB_BLOCK x NB_TRIALS_PER_BLOCK trials
#==================================================================


present_instructions(exp, INSTR_START, scale_factor)        

for block_id in range(1, NB_BLOCKS + 1):
    
    for trial_id in range(1, NB_TRIALS_PER_BLOCK + 1):

        sequence = seqs_list[(block_id-1) * NB_TRIALS_PER_BLOCK + (trial_id-1)]

        run_trial(exp, block_id, trial_id, sequence['cond'], sequence['text'], j_is_correct, fixation, hashmask, feedback_correct, feedback_incorrect, stim_text_size, bars)

        #Clear the screen before the ITI
        exp.screen.clear()
        exp.screen.update()

        #The InterTrial Interval is randomly chosen between ITI_MIN and ITI_MAX
        exp.clock.wait(random.randint(ITI_MIN, ITI_MAX))

    #Break between 2 blocks. Countdown from 30 to 0 
    if block_id != NB_BLOCKS:
        for i in range(30, 0, -1):
            text = INSTR_MID.format(block_num=block_id, NB_BLOCKS=NB_BLOCKS, countdown=i)
            instructions = stimuli.TextScreen(text=text, text_justification=0, heading="Instructions")
            present_for(exp, instructions, t=1000)


#End of the experiment 
present_instructions(exp, INSTR_END, scale_factor)

control.end()