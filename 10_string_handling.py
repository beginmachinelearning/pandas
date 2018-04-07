import pandas as pd
import numpy as np

var1="Machine"
var2="Learning"

#concat 2 strings
var3=var1+" "+var2

needle="what"
haystack="hey, what are you doing"

#Find a substring in a string
haystack.find(needle)

#index does the same thing, except that it throws an exception when not found
#find returns -1 when not found
haystack.index(needle)
haystack.index("ml")

#Check if substring present without need of index
needle in haystack
"ml" in haystack

#Check the number of occurences
haystack.count('a')
haystack.count('ey')

