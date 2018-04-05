import pandas as pd
import numpy as np


river_dict = {'river': ['Missouri', 'Mississippi', 'Yukon', 'Rio Grande', 'Arkansas'],
        'length': [2341, 2202, 1979, 1759, 1450],
        'state': ['Montana', 'Minnesota', 'British Columbia', 'Colorado', 'Kansas']}
#Override alphabetical columns and Set Column order
river_frame =pd.DataFrame(river_dict, columns=['river', 'length', 'state'], index=['river3', 'river2','river1','river4','river5',])

#Sort based on index
river_frame.sort_index()

#Sort based on values for one column
river_frame['length'].sort_values()

#Sort based on values for one column, but display all columns
river_frame.sort_values(by='length')



