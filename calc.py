import numpy as np
from loto5_40 import Reducere

#arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#or
m=10
max_intersect = 4
arr = np.arange(start=1, stop=m+1, step=1)
calc = Reducere(arr,max_intersect)
calc.go()

