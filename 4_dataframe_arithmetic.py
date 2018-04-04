import pandas as pd
import numpy as np

river_dict = {'river': ['Missouri', 'Mississippi', 'Yukon', 'Rio Grande', 'Arkansas'],
        'length': [2341, 2202, 1979, 1759, 1450],
        'state': ['Montana', 'Minnesota', 'British Columbia', 'Colorado', 'Kansas']}
river_frame =pd.DataFrame(river_dict, columns=['river', 'length', 'state'])
