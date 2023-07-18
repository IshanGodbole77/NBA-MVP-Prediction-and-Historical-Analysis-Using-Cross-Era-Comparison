import pandas as pd

df = pd.read_csv('MVP_Candidates.csv')

for i in df.index:
    if df['Seed'][i] == 0:
        df['Seed'][i] = 15
    if df['Win %'][i] == 0:
        df['Win %'][i] = 0.5
    
df.to_csv('MVP_Candidates.csv')