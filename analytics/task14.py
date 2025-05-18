import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv('train_and_test2.csv')

# Удаление пропусков
# df = df.dropna(subset=['Age', 'Fare'])
# print(df)

# Обучение модели
X = df[['Age']]
y = df['Fare']
model = LinearRegression()
model.fit(X, y)


# Предсказание
pred = model.predict(X)
plt.scatter(X, y)
plt.plot(X, pred, color='red')
plt.title('Линейная регрессия: Age vs Fare')
plt.show()
