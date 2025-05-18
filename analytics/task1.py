import pandas as pd

df = pd.read_csv('Crypto.csv')

x = df['Gas_Price_Gwei'].nunique()
print(x)

# описательная статистика:
# print(df.describe())

# 2 вариант для подсчета уник.значений в кат.столбцах:
# columns = df.select_dtypes(include=['object']).columns
# unique_counts = df[columns].nunique()
# print(unique_counts)
