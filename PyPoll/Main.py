import pandas as pd
from pathlib import Path

election_data = Path("Resources/election_data.csv")

election_data_df = pd.read_csv(election_data)

print("Election Results")
print("------------------")
print("There were " + str(len(election_data_df.index))+ " total votes")
print("------------------")

unique = election_data_df["Candidate"].unique()
totals = election_data_df['Candidate'].value_counts()
percentage = election_data_df['Candidate'].value_counts("Raymon Anthony Doane")



# for item in unique:
#     print(item)

print(totals + percentage.format)

print("------------------")
print("And the winner is... Drum Roll............... Diana Degette")
print("------------------")