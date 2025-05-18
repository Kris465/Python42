# scatter plot
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('train_and_test2.csv')
sns.scatterplot(x='Age', y='Fare', hue='2urvived', data=df)
plt.title('Age vs Fare (с учетом выживаемости)')
plt.show()
