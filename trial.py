from constants import *
from exp_utils import present_for
import expyriment.stimuli as stimuli

fixation = stimuli.FixCross()

hashmask = stimuli.TextLine("#################")

def run_trial(exp, block_id, trial_id, trial_type, sequence, j_is_correct):
    
    stim = stimuli.TextLine(sequence)

    #We display the fixation cross only for the Fixation time FixCross + Bars (= 500 ms)
    fixation.preload()
    present_for(exp, fixation, t=FIXATION_TIME_CROSS_BARS)

    #We display the bars for the fixation time FixCross + Bars plus the fixation time Bars (500ms+300ms)
    #present_for(exp, bars, t=FIXATION_TIME_BARS)
    
    #Present the sequence for 200ms 
    present_for(exp, stim, t=FIXATION_TIME_SEQUENCE)

    hashmask.present()

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
    
    #Display the feedback during TIME_FEEDBACK (= 700ms)
    feedback_text = FEEDBACK_CORRECT if correct else FEEDBACK_INCORRECT
    feedback_stim = stimuli.TextLine(feedback_text)
    present_for(exp, feedback_stim, t=TIME_FEEDBACK)