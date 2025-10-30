from expyriment.misc.constants import K_j, K_f, C_GREEN, C_RED
#================================================================
# CONSTANTS USED IN THE EXPERIMENT: FAST_SYNTAX
#================================================================

NB_BLOCKS = 5
NB_TRIALS_PER_BLOCK = 40
NB_TRIALS_TRAINING = 20

FIXATION_TIME_CROSS_BARS = 500
FIXATION_TIME_BARS = 300
FIXATION_TIME_SEQUENCE = 200
TIME_FEEDBACK = 700

#ITI is randomly chosen between ITI_MIN and ITI_MAX for each trial 
ITI_MIN = 600
ITI_MAX = 700

TRIAL_TYPES = ["normal", "scrambled"]
KEYS = [K_j, K_f]



INSTR_START = """
In this task, you have to indicate whether the meaning of a word and the color of its font match.
Press J if they do, F if they don't.\n
Press SPACE to continue.
"""
INSTR_MID = """You have finished half of the experiment, well done! Your task will be the same.\nTake a break then press SPACE to move on to the second half."""
INSTR_END = """Well done!\nPress SPACE to quit the experiment."""

FEEDBACK_CORRECT = """O"""
FEEDBACK_INCORRECT = """X"""


