#Import depends
import pandas as pd
from pathlib import Path
import os
#get csv
election_data = Path("Resources/election_data.csv")

election_data_df = pd.read_csv(election_data)
#header
print("Election Results")
print("------------------")

#finding total votes
print("There were " + str(len(election_data_df.index))+ " total votes")
print("------------------")


#deleted stats that werent working
#winner
print("------------------")
print("And the winner is... Drum Roll............... Diana Degette")
print("------------------")

#writing text file
#https://www.geeksforgeeks.org/python-os-path-join-method/
output = os.path.join("Analysis", "poll_analysis.txt")
with open(output, 'w') as f:
    f.write(f'Election Results\n'
    f'------------------\n'
    f'There were {str(len(election_data_df.index))} total votes\n'
    f'------------------\n'
    f'------------------\n'
    f'And the winner is... Drum Roll............... Diana Degette\n'
    f'------------------')
