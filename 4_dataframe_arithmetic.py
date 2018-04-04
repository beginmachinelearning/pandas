import pandas as pd
import numpy as np

my_df=pd.DataFrame(np.arange(10))

#Add 1
my_df.add(1)

#Sub 1
my_df.sub(1)

#reverse sub
my_df.rsub(1)

#Divide
my_df.div(2)

#Reverse Divide
my_df.rdiv(1)

#Multiply
my_df.mul(10)

#Exponent
my_df.pow(2)

#Using NumPy Abs
np.abs(my_df.sub(10))