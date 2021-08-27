Reduced scheme for Lotttery 5 from 40

Requirements are python 3 and numpy.

Select a reduced set (a local min anyway) of combination of 5 numbers (m choose 5) (from m <= 40) which have at least max_intersect common numbers with any combination of 6 numbers chosen from the m chosen numbers (m choose 6), using either as criterion of selection, maxim number of c6 covered or minimul standard deviation of intersections sums between solutions (c5) and c6 combinations.

For example (edit calc.py):

#arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#or

m=10

max_intersect = 4

nsigma = 100 #that means that all c6 will be processed
#if nsigma = 1 or 2 for example, will be used only c6 between 1 or 2 std deviations (which are less likely to be chosen)  which result in a smaller matrix intersections and more computing power

arr = np.arange(start=1, stop=m+1, step=1)

calc = Reducere(arr,max_intersect,nsigma)

calc.go(criterion='max',max_cover='-')

#calc.go(criterion='stddev',max_cover=100)

gives a scheme of 10 numbers:

(1, 2, 3, 4, 5)

(1, 6, 7, 8, 9)

(2, 3, 6, 7, 10)

(4, 5, 8, 9, 10)

(1, 2, 3, 4, 10)

(1, 5, 6, 7, 10)

(2, 3, 4, 5, 6)

(1, 2, 3, 7, 8)

(1, 2, 3, 4, 5)

Any combination of 6 numbers from 1...10 will intesect at least one the above sets with at least 4 common numbers


Additional tools:

intersect.py generates c5 which had only 2 numbers in common (at most) with themselfes.

Modify m in script (max number in the set).

For big sets (~ m > 15-20), depending on the hardware, the state is saved in 'data_c5.bin' and could be resumed the process if script stopped anytime. 

If m changed, delete data_c5.bin!

This file retain choosed c5 indexes in pickle bin format.

For retrieve solution, just comment go() procedure and activate interpret().

cover() gives all c6 that have at least 4 common numbers with c5 chosen above.

