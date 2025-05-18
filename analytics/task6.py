# столбчатые диаграммы
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('train_and_test2.csv')
sns.countplot(x='Pclass', data=df)
plt.title('Количество пассажиров по классам')
plt.show()
