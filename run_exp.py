from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_j, K_f
import random
from constants import *
from exp_utils import *
from trial import *


sequences = ["je veux du pain", 
            "est beau abri ton",
            "un peu de vin",
            "pain du je veux",
            "il vend du miel",
            "ce quoi soit que",
            "tout abus sera puni",
            "fer une en clef",
            "le toît est bleu",
            "fer une en clef"]

trial_types_ = [
    "normal",
    "scrambled", 
    "normal",
    "scrambled",
    "normal",
    "scrambled",
    "normal",
    "scrambled",
    "normal",
    "scrambled"
]



""" Global settings """
exp = design.Experiment(name="Stroop", background_colour=C_WHITE, foreground_colour=C_BLACK)
exp.add_data_variable_names(['block_cnt', 'trial_cnt', 'trial_type', 'word', 'color', 'RT', 'correct'])

control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
fixation = stimuli.FixCross()
fixation.preload()



control.start(subject_id=1)

for block_id in range(1, 1 + 1):
    for trial_id in range(1, len(sequences) + 1):
        sequence = sequences[trial_id-1]
        trial_type = trial_types_[trial_id-1]
        j_is_correct = True
        run_trial(exp, block_id, trial_id, trial_type, sequence, j_is_correct)
   #if block_id != NB_BLOCKS:
    #    present_instructions(INSTR_MID)
#present_instructions(INSTR_END)

control.end()