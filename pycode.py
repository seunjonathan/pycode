import pandas as pd
import numpy as np
import unittest
df = pd.read_csv("C:\\Users\\seunj\\Documents\\Datasets\\rccg\\csv\\May2022payment.csv")
print(df.head(3))
df = df.drop(columns=['channel','gateway'])
cols = list(df.columns.values)
print(cols)
#df.groupby('paymenttype')
print(df.head())
df.describe()