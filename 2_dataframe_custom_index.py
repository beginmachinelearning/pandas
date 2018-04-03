import pandas as pd
import numpy as np

river_dict = {'river': ['Missouri', 'Mississippi', 'Yukon', 'Rio Grande', 'Arkansas'],
        'length': [2341, 2202, 1979, 1759, 1450],
        'state': ['Montana', 'Minnesota', 'British Columbia', 'Colorado', 'Kansas']}
river_frame = pd.DataFrame(river_dict, index=['river1', 'river2','river3','river4','river5',])

#Look up by index
river_frame.loc['river1']
river_frame.iloc[0, :]