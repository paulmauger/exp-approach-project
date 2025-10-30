import math
from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK

FPS  = 60  
MSPF = 1000 / FPS 

def to_frames(t): 
    return math.ceil(t / MSPF) 

def to_time(num_frames): 
    return num_frames * MSPF 

def load(stims): 
    for stim in stims: 
        stim.preload()

def timed_draw(exp, *stims):
    t0 = exp.clock.time
    exp.screen.clear()
    for stim in stims:
        stim.present(clear=False, update=False)
    exp.screen.update()
    t1 = exp.clock.time
    return t1 - t0

def present_for(exp, *stims, t=1000):
    dt = timed_draw(exp, *stims)
    exp.clock.wait(t - dt)
