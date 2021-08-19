import numpy as np
from loto5_40 import Reducere

#arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#or
m=10
max_intersect = 4
#if nsigma = 1 or 2 for example, will be used only c6 between 1 or 2 std deviations (which are less likely to be chosen)  which result in a smaller matrix intersections and more computing power
nsigma = 200 #that means that all c6 will be processed
arr = np.arange(start=1, stop=m+1, step=1)
calc = Reducere(arr,max_intersect,nsigma)
calc.go(criterion='max',max_cover='-')
#calc.go(criterion='stddev',max_cover=95)
