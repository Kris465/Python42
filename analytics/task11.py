import pandas as pd

df = pd.read_csv('sales_data.csv')

df['Date'] = pd.to_datetime(df['Sale_Date'])
# df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month
df['DayOfWeek'] = df['Date'].dt.day_name()
print(df['DayOfWeek'])
print(df['Month'])
