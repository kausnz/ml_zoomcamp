import numpy as np
import pandas as pd

df = pd.read_csv('data.csv')

# Question 1
print(np.__version__)

# Question 2
print(df.shape[0])

# Question 3
print(df.groupby('Make').size().sort_values(ascending=False).head(3))

# Question 4
print(df[df['Make']=='Audi'].drop_duplicates(subset='Model').shape[0])

# Question 5
print(df.columns[df.isnull().any().to_list()])

# Question 6
median_engine_cylinders = df['Engine Cylinders'].median()
median_engine_cylinders #6.0
mode_engine_cylinders = df['Engine Cylinders'].mode()
mode_engine_cylinders # 4.0
df['Engine Cylinders'] = df['Engine Cylinders'].fillna(mode_engine_cylinders)
median_engine_cylinders_after = df['Engine Cylinders'].median()
print("Median before = {}, median after = {}".format(median_engine_cylinders, median_engine_cylinders_after))

# Question 7
lotus_cars = df[df['Make'] == 'Lotus']
lotus_cars.shape
X = lotus_cars[['Engine HP', 'Engine Cylinders']].drop_duplicates().to_numpy()
Xt = X.transpose()
XTX = Xt.dot(X)
XTX_inv = np.linalg.inv(XTX)
y = np.array([1100, 800, 750, 850, 1300, 1000, 1000, 1300, 800])
w = XTX_inv.dot(Xt).dot(y)
print(w[0].round(4))
