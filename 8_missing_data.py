import pandas as pd
import numpy as np


df=pd.read_csv("datasets/titanic.csv")

#Check which column has null values, .any is used to check for True
df.columns[df.isna().any()]

#Delete row when any columns is empty
df=df.dropna()

#Delete row only when value in a certain column is empty
df=df['Age'].dropna()