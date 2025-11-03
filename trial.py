from constants import *
from exp_utils import present_for
import expyriment.stimuli as stimuli
from expyriment.misc.constants import K_j, K_f

def run_trial(exp, block_id, trial_id, trial_type, sequence, j_is_correct, fixation, hashmask, feedback_correct, feedback_incorrect, stim_text_size, bars):
    
    stim = stimuli.TextLine(sequence, text_size=stim_text_size)

    #We display the fixation cross only for the Fixation time FixCross + Bars 
    present_for(exp, fixation, *bars, t=FIXATION_TIME_CROSS_BARS)

    #We display the bars for the fixation time FixCross + Bars plus the fixation time Bars
    present_for(exp, *bars, t=FIXATION_TIME_BARS)
    
    #Present the sequence for 200ms 
    present_for(exp, stim, *bars, t=FIXATION_TIME_SEQUENCE)

    present_for(exp, hashmask, *bars, t=0) #t=0 so it just prints the mask+bars and wait for the key

    key, rt = exp.keyboard.wait(KEYS)
    
    #The answer is correct if: 
    # - The key to press if correct is J, J is pressed and the condition is normal 
    # - The key to press if correct is J, F is pressed and the condition is scrambled
    # - The key to press if correct is F, J is pressed and the condition is scrambled 
    # - The key to press if correct is F, F is pressed and the condition is normal 
    expected_key = (K_j if j_is_correct else K_f) if trial_type == "normal" else (K_f if j_is_correct else K_j)
    correct = (key == expected_key)
    
    #Add the data to the logs in /data 
    exp.data.add([block_id, trial_id, trial_type, sequence, rt, correct])
    
    #Display the feedback during TIME_FEEDBACK 
    feedback_stim = feedback_correct if correct else feedback_incorrect
    present_for(exp, feedback_stim, t=TIME_FEEDBACK)
