import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data_business_data.csv")

X = df[['marketing_spend', 'operations_cost']]
y = df['revenue']

model = LinearRegression().fit(X, y)

def simulate(marketing, ops):
    return model.predict([[marketing, ops]])[0]