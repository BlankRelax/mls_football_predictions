import pandas as pd

df = pd.read_csv('USA.csv')
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
df['year'] = df['Date'].dt.year
#df['month'] = df['Date'].dt.month
#df['day'] = df['Date'].dt.day

fitset = df[df.year<=2015] # its ok just to filter on year since last game of 2015 was played on 06/12/2015
print(fitset.head())
df['home_conference'] =

