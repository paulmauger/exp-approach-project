import math, csv, random
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

def present_instructions(exp, text, scale_instructions=1):
    instructions = stimuli.TextScreen(text=text, text_justification=0, heading="Instructions", text_size=int(20*scale_instructions))
    instructions.present()
    exp.keyboard.wait()

def present_instructions_for(exp, text, t=1000, scale_instructions=1):
    instructions = stimuli.TextScreen(text=text, text_justification=0, heading="Instructions", text_size=int(20*scale_instructions))
    dt = present_for(exp, instructions, t=t)
    exp.clock.wait(t - dt)


def load_csv(path):
    """ 
    Load the csv and store in a list of dictionaries. 
    Each dictionary contains one row of the csv with the column names as key and the entries as values.
        
    Arguments:
        -- path (string): The path to the CSV file.

    """

    rows = []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append({k: v.strip() for k, v in r.items()})
    return rows


def shuffle_list(list_seqs, max_repetitions=3):
    """Construct a list of sequences
    with at most max_repetitions of the same condition consecutively."""
    
    random.shuffle(list_seqs)

    res = []
    len_list = len(list_seqs)

    #Half of the elements are 0 (normal), half are 1 (scrambled)
    counts = {0: len_list//2, 1: len_list//2}

    last = None
    streak = 0 #consecutive streak of normal or scrambled

    normal_pointer = 0 
    scrambled_pointer = 0

    #While there is still a condition to add, we compute which condition we can possibly add at this step
    #randomly choose of them (if there is any, otherwise we restart) and add the corresponding condition to the list.
    while counts[0] > 0 or counts[1] > 0:
        choices = []
        for val in [0, 1]:
            if counts[val] > 0:
                #You can choose this val if either:
                #- it's not the same as last, or
                #- streak < max_repetitions
                if val != last or streak < max_repetitions:
                    choices.append(val)

        if not choices:
            #restart if dead-end
            return shuffle_list(list_seqs, max_repetitions)

        choice = random.choice(choices)
        
        #If we choose 0 then add a normal sequence to the list, else a scrambled one
        #more precisely the first sequence corresponding to the wanted condition in the list (scanning the list)
        if choice == 0:
            while list_seqs[normal_pointer]['cond'] != 'normal':
                normal_pointer += 1
            res.append(list_seqs[normal_pointer])
            normal_pointer += 1
        
        elif choice == 1:
            while list_seqs[scrambled_pointer]['cond'] != 'scrambled':
                scrambled_pointer += 1
            res.append(list_seqs[scrambled_pointer])
            scrambled_pointer += 1

        #There is one less normal or scrambled (choice) sequence to add in the list
        counts[choice] -= 1

        #Update the streak and keep the last choice in memory (last) to update at the next step 
        if choice == last:
            streak += 1
        else:
            streak = 1
        last = choice
    
    return res