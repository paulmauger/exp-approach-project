from expyriment.misc.constants import K_j, K_f, C_GREEN, C_RED
import expyriment.stimuli as stimuli

#================================================================
# CONSTANTS USED IN THE EXPERIMENT: FAST_SYNTAX
#================================================================

NB_BLOCKS = 5
NB_TRIALS_PER_BLOCK = 40
NB_TRIALS_TRAINING = 20

NB_SEQUENCES_TRAINING = 20
NB_SEQUENCES_TRIALS = 200

#Assertions to make sure the number of sequences can actually be reached
assert NB_TRIALS_TRAINING <= NB_SEQUENCES_TRAINING
assert NB_TRIALS_PER_BLOCK*NB_BLOCKS <= NB_SEQUENCES_TRIALS


FIXATION_TIME_CROSS_BARS = 500
FIXATION_TIME_BARS = 300
FIXATION_TIME_SEQUENCE = 200
TIME_FEEDBACK = 700

#ITI is randomly chosen between ITI_MIN and ITI_MAX for each trial 
ITI_MIN = 600
ITI_MAX = 700

TRIAL_TYPES = ["normal", "scrambled"]
KEYS = [K_j, K_f]



INSTR_TRAINING_J_CORRECT = """
In this task, you have to indicate whether the presented sequence is grammatically correct or not.
Press J if it is, F if it's not.\n
During the experiment, please fixate between the fixation bars and minimize blinks, eye-movements, and body movements.\n
Press any key to start the training.
"""

INSTR_TRAINING_F_CORRECT = """
In this task, you have to indicate whether the presented sequence is grammatically correct or not.
Press F if it is, J if it's not.\n
During the experiment, please fixate between the fixation bars and minimize blinks, eye-movements, and body movements.\n
Press any key to start the training.
"""

INSTR_END_TRAINING = """Well done! You have completed the training. \nPress SPACE to continue to the experiment."""


INSTR_START_J_CORRECT = """
In this task, you have to indicate whether the presented sequence is grammatically correct or not.
Press J if it is, F if it's not.\n
During the experiment, please fixate between the fixation bars and minimize blinks, eye-movements, and body movements.\n
Press any key to continue.
"""

INSTR_START_F_CORRECT = """
In this task, you have to indicate whether the presented sequence is grammatically correct or not.
Press F if it is, J if it's not.\n
During the experiment, please fixate between the fixation bars and minimize blinks, eye-movements, and body movements.\n
Press any key to continue.
"""

INSTR_MID = """Block {block_num}/{NB_BLOCKS} ended, well done! Your task will be the same.\nTake a break. The next block will start in {countdown} seconds."""
INSTR_END = """Well done! You have completed the experiment. \nPress SPACE to quit."""
