import numpy as np

from scipy.sparse import csr_matrix

dense_a = np.zeros((3, 3), dtype = np.int8)
dense_a[0,0] = 1
dense_a[1,1] = 1
dense_a[2,2] = 1
print(dense_a)

sparse_a = csr_matrix(dense_a)
#A = csr_matrix([[1, 2, 0], [0, 0, 3], [4, 0, 5]])
print("retroversion")
print(csr_matrix.toarray(sparse_a))
print(sparse_a.todense())
print("--------------")

dense_b = np.array([1, 0, -1])
sparse_b = csr_matrix(dense_b)

print("dot product")
print(dense_a@dense_b)
print("?")
print(sparse_a.dot(dense_b))
print("?")
print(csr_matrix(sparse_a).multiply(csr_matrix(sparse_b)).todense())
