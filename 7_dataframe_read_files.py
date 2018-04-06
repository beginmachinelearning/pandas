import pandas as pd
import numpy as np

df=pd.read_csv("datasets/Social_Network_Ads.csv")

#First row of data incorrectly becomes header
df=pd.read_csv("datasets/Social_Network_Ads_no_header.csv")

#Tell the Dataframe this csv has no header row
df=pd.read_csv("datasets/Social_Network_Ads.csv", header=None)

#Set one column as index column
df=pd.read_csv("datasets/Social_Network_Ads.csv", index_col='User ID')


#Read from text file using separator
df=pd.read_csv("datasets/text_single_space.txt", sep=" ")


#Does not work for irregular spaces
df=pd.read_csv("datasets/text_data.txt", sep=" ")

#Read from text file using separator
df=pd.read_csv("datasets/text_data.txt", delim_whitespace=True)

#Write to a file
df.to_csv("datasets/write_csv.csv")


df=pd.read_csv("datasets/Social_Network_Ads.csv")

#Write to a file, only specific columns
df.to_csv("datasets/write_csv.csv", columns=['Gender', 'Age'])