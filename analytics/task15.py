import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('train_and_test2.csv')
# Сохранение датафрейма
df.to_csv('train_and_tast2.csv', index=False)

# Сохранение графика
plt.savefig('plot.png')
