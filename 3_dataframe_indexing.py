import pandas as pd
import numpy as np

singled_dataframe = pd.DataFrame(np.arange(1,10))

#Access 1st row
singled_dataframe.iloc[0]
#Access 6th row
singled_dataframe.iloc[5]

#Access rows 1 to 5
singled_dataframe.iloc[0:5]

#Access rows 1 to 5
singled_dataframe.iloc[:-1]

river_dict = {'river': ['Missouri', 'Mississippi', 'Yukon', 'Rio Grande', 'Arkansas'],
        'length': [2341, 2202, 1979, 1759, 1450],
        'state': ['Montana', 'Minnesota', 'British Columbia', 'Colorado', 'Kansas']}
river_frame =pd.DataFrame(river_dict, columns=['river', 'length', 'state'])


#Access all rows and columns
river_frame.iloc[:, :]


#Access 2nd column of all rows
river_frame.iloc[:, 1]

#Access 2nd, 3rd column of all rows
river_frame.iloc[:, 1:3]

#Access last column
river_frame.iloc[:, -1]

#Access 2nd, 3rd row and 1st, 2nd column
river_frame.iloc[1:3, 0:2]