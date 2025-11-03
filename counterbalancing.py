#==================================================================
# COUNTERBALANCING: 
# For each row i in the CSV, randomly assign the normal sequence to 
# List A and the scrambled sequence to List B or vice versa.
# Generate the List_A.csv and List_B.csv files in tables/
#==================================================================

import csv
import random
from exp_utils import load_csv



def make_counterbalanced_lists(seqs_rows):
    """
    Create the lists List_A and List_B based on the initial 200 normal+scrambled sequences (Table_S1_Experiment1.csv).
    """
    n = len(seqs_rows)
    flips = [None] * n
    need = n // 2
    choices = [True] * need + [False] * (n - need)
    random.shuffle(choices)

    for i in range(n):
        flips[i] = choices[i]
    
    listA = []
    listB = []
    
    for i, row in enumerate(seqs_rows):
        if flips[i]:
            listA.append({'item': i, 'text': row['normal'], 'cond': 'normal'})
            listB.append({'item': i, 'text': row['scrambled'], 'cond': 'scrambled'})
        else:
            listA.append({'item': i, 'text': row['scrambled'], 'cond': 'scrambled'})
            listB.append({'item': i, 'text': row['normal'], 'cond': 'normal'})
    
    return listA, listB



def write_counterbalanced_csv(listA, listB):
    """
    Write List_A.csv and List_B.csv based on the lists listA and listB from make_counterbalanced_lists().
    """

    fieldnames = ['item', 'text', 'cond']

    with open("tables/List_A.csv", 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(listA)
    
    with open("tables/List_B.csv", 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(listB)


random.seed(987654321)

#seqs_rows = [{"normal": "je veux du pain", "scrambled": "pain du je veux"}, ...]
seqs_rows = load_csv('tables/Table_S1_Experiment1.csv') 

listA, listB = make_counterbalanced_lists(seqs_rows)

write_counterbalanced_csv(listA, listB)
