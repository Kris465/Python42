import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

df = pd.read_csv('train_and_test2.csv')
# sns.boxplot(df['Fare'])
# plt.title('Выбросы в Fare')
# plt.show()

df = df[df['Fare'] <= 300]
