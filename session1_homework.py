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
mode_engine_cylinders = df['Engine Cylinders'].mode()
print(mode_engine_cylinders)
df['Engine Cylinders'].fillna(mode_engine_cylinders, inplace=True)
median_engine_cylinders_after = df['Engine Cylinders'].median()
print(df.columns[df.isnull().any().to_list()])
print("Median before = {}, median after = {}".format(median_engine_cylinders, median_engine_cylinders_after))

# Question 7 (incomplete)
lotus_cars = df[df['Make'] == 'Lotus']
X = lotus_cars[['Engine HP', 'Engine Cylinders']].drop_duplicates().to_numpy()
Xt = X.transpose()
print(Xt)
XTX = Xt @ X
XTX_inv = np.linalg.inv(XTX)
print(XTX_inv)
y = np.array([1100, 800, 750, 850, 1300, 1000, 1000, 1300, 800])

# result = y.dot(Xt.dot(XTX_inv))
print(result)