# круговые диаграммы
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('train_and_test2.csv')
df['2urvived'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Соотношение выживших и погибших')
plt.ylabel('')
plt.show()
