import pandas as pd

df = pd.read_csv('MVP_Candidates_Complete.csv')

Pos_No = pd.Series([])

for i in range(len(df)):
    if df["Pos"][i] == "PG":
        Pos_No[i] = 1
    elif df["Pos"][i] == "SG":
        Pos_No[i] = 2
    elif df["Pos"][i] == "SF":
        Pos_No[i] = 3
    elif df["Pos"][i] == "PF":
        Pos_No[i] = 4
    elif df["Pos"][i] == "C":
        Pos_No[i] = 5
    else:
        Pos_No[i] = 0

df.insert(2, "Pos_No", Pos_No)

df.to_csv('MVP_Candidates.csv')