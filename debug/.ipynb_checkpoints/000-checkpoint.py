#https://stackoverflow.com/questions/36782588/dot-product-sparse-matrices

a = np.arange(12).reshape(3,4)
a1 = sparse.csr_matrix(a)

np.dot(a, a.T)
a1 * a.T
a*a
a1.multiply(a1)
