import pandas as pd
import numpy as np

river_dict = {'river': ['Missouri', 'Mississippi', 'Yukon', 'Rio Grande', 'Arkansas'],
        'length': [2341, 2202, 1979, 1759, 1450],
        'state': ['Montana', 'Minnesota', 'British Columbia', 'Colorado', 'Kansas']}
river_frame = pd.DataFrame(river_dict)

# Display first 5 rows
river_frame.head()

#Choose only 1 column
river_frame['length']

#Look at some numeric stats
river_frame.describe()

#Add new column with numeric value
river_frame['additional_column'] = np.arange(5)

river_frame.describe()

river_frame['length'].describe()

#delete a column
del river_frame['additional_column']

#create new column with conditional value
river_frame['huge_river']=river_frame['length']>=1800

#Transpose
river_frame.T