import numpy as np
from loto5_40 import Reducere

#arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
m = 11
arr = np.arange(start=1, stop=m, step=1)
calc = Reducere(arr)
calc.go()
