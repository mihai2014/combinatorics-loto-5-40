Reduced scheme for Loto 5 from 40

Requirements are python 3 and numpy.

Select a reduced set of combination of 5 numbers (m choose 5) (from m <= 40) which have at least 4 common numbers with any combination of 6 numbers chosen from the m chosen numbers (m choose 6).

For example:

m=11

arr = np.arange(start=1, stop=m, step=1)

calc = Reducere(arr)

calc.go()


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
