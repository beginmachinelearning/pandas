import pandas as pd
import numpy as np


titanic_df=pd.read_csv("datasets/titanic.csv")

#Count how many duplicates
(titanic_df['Age'].duplicated()==True).tolist().count(True)

df_single=pd.DataFrame([1, 2, 2, 5,4, 1 , 8, 9, 10])

#Drop all duplicate rows
df_single.drop_duplicates(inplace=True)

#Dropping multi columnar data needs common values for all columns, or a row that is exactly the same
#Below statement does not delete any row because no row is duplicated
titanic_df.drop_duplicates(inplace=True)

#Get River data with row 1 and row 2 exactly same
river_dict = {'river': ['Missouri', 'Missouri', 'Yukon', 'Rio Grande', 'Arkansas'],
        'length': [2341, 2341, 1979, 1759, 1450],
        'state': ['Montana', 'Montana', 'British Columbia', 'Colorado', 'Kansas']}

river_frame =pd.DataFrame(river_dict, columns=['river', 'length', 'state'], index=['river1', 'river2','river3','river4','river5',])

#This line deletes the duplicated row, by default retains the first occurence
river_frame.drop_duplicates(inplace=True)

#This line deletes the duplicated row, but retains the last occurence this time
river_frame.drop_duplicates(inplace=True, keep='last')

bins = [0, 15, 30, 45, 60, 80]
age_brackets = pd.cut(titanic_df['Age'], bins)
#Create new column for age bracket based on Age segragated into bins
titanic_df['AgeBracket']=pd.cut(titanic_df['Age'], [0, 15, 50, 80], labels=['15 and below', 'From 16 to 50', 'Above 50'])

#Create 4 equal ranged bins
age_brackets_4 = pd.cut(titanic_df['Age'], 4)
age_brackets_4.value_counts()