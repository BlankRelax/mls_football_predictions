import pandas as pd

df = pd.read_csv('USA.csv')
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
df['year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month
df['day'] = df['Date'].dt.day

fitset = df[df.year<=2015]
print(fitset.to_string())

