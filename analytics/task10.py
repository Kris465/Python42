# график временного ряда
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('sales_data.csv')
df['Date'] = pd.to_datetime(df['Sale_Date'])
# df_sorted = df.sort_values('Date', ascending=False)
df.set_index('Date')['Sales_Amount'].plot()
plt.title('Динамика продаж')
plt.show()
# print(df_sorted.head(10))
