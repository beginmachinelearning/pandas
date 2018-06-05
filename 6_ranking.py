import pandas as pd
import numpy as np
import random

my_array = pd.Series(np.random.randint(0, 100, 10))

#Show the ranking of each element(where it stands if sorted)
my_array.rank()


my_array_with_duplicates=pd.Series([3, 2, 5, 3, 7, 2, 6, 8, 9, 11])

my_array_with_duplicates.rank()

#3 repitions does not show a .666
my_array_with_duplicates=pd.Series([3, 2, 5, 3, 7, 2, 2, 2, 9, 11])

my_array_with_duplicates.rank()
