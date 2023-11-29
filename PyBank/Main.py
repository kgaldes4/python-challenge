#Import depends
import pandas as pd
from pathlib import Path
import os
#get csv
budget_data = Path("Resources/budget_data.csv")
#read csv
budget_data_df = pd.read_csv(budget_data)
#calc for later
budget_data_df["Profit/Loss Change"] = budget_data_df["Profit/Losses"].diff()
#header
print("Financial Analysis")
print("------------------")
#finding total months in dataset
print("There are a total of " + str(len(budget_data_df.index)) 
 +" months in the dataset")
#finding profit loss sum
print("The total profit/loss is $" + str(budget_data_df["Profit/Losses"].sum()))
#finding avg, max min of profit loss  change

print("The total average change is $" + str(budget_data_df["Profit/Loss Change"].mean()))
print("The greatest increase is $" + str(budget_data_df["Profit/Loss Change"].max()))
print("The greatest decrease is $" + str(budget_data_df["Profit/Loss Change"].min()))

#writing text file
#https://www.geeksforgeeks.org/python-os-path-join-method/
output = os.path.join("Analysis", "budget_analysis.txt")
with open(output, 'w') as f:
    f.write(f'Financial Analysis\n'
    f'------------------\n'
    f'There are a total of {str(len(budget_data_df.index))}  months in the dataset\n'

    f'The total profit/loss is $ {str(budget_data_df["Profit/Losses"].sum())}\n'
    f'The total average change is $ {str(budget_data_df["Profit/Loss Change"].mean())}\n'
    f'The greatest increase is $ {str(budget_data_df["Profit/Loss Change"].max())}\n'
    f'The greatest decrease is $ {str(budget_data_df["Profit/Loss Change"].min())}')

   

