import pandas as pd
from pathlib import Path

budget_data = Path("Resources/budget_data.csv")

budget_data_df = pd.read_csv(budget_data)

print("Financial Analysis")
print("------------------")
print("There are a total of " + str(len(budget_data_df.index)) 
      +" months in the dataset")

print("The total profit/loss is $" + str(budget_data_df["Profit/Losses"].sum()))

budget_data_df["Profit/Loss Change"] = budget_data_df["Profit/Losses"].diff()
print("The total average change is $" + str(budget_data_df["Profit/Loss Change"].mean()))
print("The greatest increase is $" + str(budget_data_df["Profit/Loss Change"].max()))
print("The greatest decrease is $" + str(budget_data_df["Profit/Loss Change"].min()))