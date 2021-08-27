import numpy as np
import scipy.sparse

sparse_matrix = scipy.sparse.csc_matrix(np.array([[0, 0, 3], [4, 0, 0]]))
#print(sparse_matrix)
#print(sparse_matrix.todense())
scipy.sparse.save_npz('/tmp/sparse_matrix.npz', sparse_matrix)
sparse_matrix = scipy.sparse.load_npz('/tmp/sparse_matrix.npz')
#print(sparse_matrix)
#print(sparse_matrix.todense())

#A = np.ones([10,10])
#Al = A.tolil()
#Al[5,7] = 6  # the normal 2d matrix indexing notation
#print(Al)
#print(Al.A) # aka Al.todense()
#A1 = Al.tobsr()  # if it must be in bsr format

import numpy as np
from scipy.sparse import bsr_matrix, csr_matrix, lil_matrix

#row = np.array( [5] )
#col = np.array( [7] )
#data = np.array( [6] )
#print(row,col,data)
#A = csr_matrix( (data,(row,col)) )
#print(A.todense())

dense_a = np.zeros([10,10],dtype=np.int8)
lil_a = lil_matrix(dense_a)
lil_a[2,2] = 1
print(lil_a.todense())
scipy.sparse.save_npz('/tmp/sparse_matrix.npz', lil_a)
sparse_matrix = scipy.sparse.load_npz('/tmp/sparse_matrix.npz')
#print(sparse_matrix)
print(sparse_matrix.todense())

