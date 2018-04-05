import pandas as pd
import numpy as np

df=pd.read_csv("datasets/Social_Network_Ads.csv")

#First row of data incorrectly becomes header
df=pd.read_csv("datasets/Social_Network_Ads_no_header.csv")

#Tell the Dataframe this csv has no header row
df=pd.read_csv("datasets/Social_Network_Ads.csv", header=None)