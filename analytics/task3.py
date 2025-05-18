import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# гистограмма возрастов
df = pd.read_csv('train_and_test2.csv')
# z = df['Age'].hist(bins=20)
# plt.title('Распределение возрастов')
# plt.xlabel('Age')
# plt.ylabel('Count')
# plt.show()
# print(z)

# распр-е цен билетов

sns.boxplot(x='2urvived', y='Fare', data=df)
plt.title('Fare vs 2urvived')
plt.show()
