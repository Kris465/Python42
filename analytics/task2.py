import pandas as pd

# df = pd.read_csv('Crypto.csv')
# x = pd.crosstab(df['Transaction_ID'], df['Currency'])
# print(x)

df = pd.read_csv('train_and_test2.csv')
y = df.groupby('Pclass')['2urvived'].mean() * 100
print(y)
