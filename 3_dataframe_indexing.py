import pandas as pd
import numpy as np

singled_dataframe = pd.DataFrame(np.arange(1,10))

#Access 1st row
singled_dataframe.iloc[0]
#Access 6th row
singled_dataframe.iloc[5]

#Access rows 1 to 5
singled_dataframe.iloc[0:5]