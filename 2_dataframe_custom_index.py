import pandas as pd
import numpy as np

river_dict = {'river': ['Missouri', 'Mississippi', 'Yukon', 'Rio Grande', 'Arkansas'],
        'length': [2341, 2202, 1979, 1759, 1450],
        'state': ['Montana', 'Minnesota', 'British Columbia', 'Colorado', 'Kansas']}
river_frame = pd.DataFrame(river_dict, index=['river1', 'river2','river3','river4','river5',])
#Override alphabetical columns and Set Column order
river_frame =pd.DataFrame(river_dict, columns=['river', 'length', 'state'], index=['river1', 'river2','river3','river4','river5',])

#Look up by label index
river_frame.loc['river1']

#Get all indices
river_frame.index

#Add a new row
river_frame.loc['river6']=[  'Brazos', 860,'Texas']



duplicate_index = pd.Series(range(5), index=['index1', 'index1', 'index2', 'index2', 'indexn'])

#Access a duplicate index
duplicate_index.loc['index1']

#update a duplicate index
duplicate_index.loc['index1']=10

#Add a new river with same index
river_frame.loc['river6']=['Green', 760, 'Wyoming']

reindexed=river_frame.reindex(['index1', 'index2', 'index3', 'index4', 'index5'])

