# boxplot
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('train_and_test2.csv')
sns.boxplot(x='Pclass', y='Age', data=df)
plt.title('Age по классам')
plt.show()
