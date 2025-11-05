# CORE-1: Fast Syntax in the brain (Experiment)

This repository contains the Python code to reproduce the first experiment of the paper: 
> Wen, Y., Mirault, J., & Grainger, J. (2021). Fast syntax in the brain: Electrophysiological evidence from the rapid parallel visual presentation paradigm (RPVP). Journal of Experimental Psychology: Learning, Memory, and Cognition, 47(1), 99–112. https://doi.org/10.1037/xlm0000811 


##

The experiment uses the **Rapid Parallel Visual Presentation (RPVP)** paradigm to study syntactic processing.

In the task, the participants have to indicate whether the presented 4-word sequence is grammatically correct or not. The two conditions are *Normal* and *Scrambled* sequences. 

The training consists of **20 trials** (`tables/List_Training.csv`).

The main experiment is **200 trials** (`tables/List_Experiment.csv`), with short breaks every 40 trials.





## Dependencies 

This code uses the Python library `Expyriment` (https://docs.expyriment.org) to run the experiment. 
* **[Installation Guide](https://docs.expyriment.org/Installation.html)**

## How to run the experiment: 

You can run the experiment from your terminal using `python3 run_exp.py` with the following arguments:

*   `--id <number>`: **Participant ID** (e.g., `--id 1`). Defaults to `1`.
*   `--mode <mode>`: **Experiment mode**. Can be `full`, `experiment` or `train`. Defaults to `full`.
*   `--fullscreen`: **Display mode**. Add this flag to run in fullscreen.

### Full Experiment (Default)
- To run the **full experiment** (training + experiment) for the first participant in fullscreen, execute: 
```bash
python3 run_exp.py --mode full --id 1 --fullscreen
```

which is equivalent to:
```bash
python3 run_exp --fullscreen
```

### Training

- To run only the **training trials**, execute: 
```bash
python3 run_exp --mode train
```

### Experiment blocks

- To run only the **main experiment blocks**, execute: 
```bash
python3 run_exp --mode experiment
```


## Project Authors
CORE-1 coding project by 
Elizaveta S., Anna M., Claire L., Paul M.

*(cog-SUP 2025-2026.)*