import pandas as pd

df = pd.read_csv('train_and_test2.csv')
x = pd.pivot_table(df, index='Pclass', columns='Sex', values='2urvived',
                   aggfunc='mean')
print(x)
