import pandas as pd
import numpy as np


df=pd.read_csv("datasets/titanic.csv")

#Check which column has null values, .any is used to check for True
df.columns[df.isna().any()]

#Delete row when any columns is empty
df=df.dropna()

#Delete row only when value in a certain column is empty
df=df['Age'].dropna()

#Getting all data again
df=pd.read_csv("datasets/titanic.csv")

#Check which column has null values, .any is used to check for True
df.columns[df.isna().any()]

# Returns a new object, does not affect df 
df['Age'].fillna(0)


# Modifies the df object in place
df['Age'].fillna(0, inplace=True)

#Fill empty values, also another way of reassigning values back to the column manually
df['Age']=df['Age'].fillna(0)

df=pd.read_csv("datasets/titanic.csv")
#Fill empty values in different columns with different values
df=df.fillna({'Age': 0, 'Cabin': 1, 'Embarked':'S'})

df=pd.read_csv("datasets/titanic.csv")
#Fill a column using a operation
df=df.fillna({'Age': df['Age'].mean(), 'Cabin': 1, 'Embarked':'S'})
