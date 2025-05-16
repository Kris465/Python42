import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('train_and_test2.csv')

# corr_matrix = df[['Age', 'Fare', 'sibsp', 'Parch']].corr()
# sns.heatmap(corr_matrix, annot=True)
# plt.title('Корреляции числовых признаков')
# plt.show()

sns.scatterplot(x='Age', y='Fare', data=df)
plt.title('Age vs Fare')
plt.show()
