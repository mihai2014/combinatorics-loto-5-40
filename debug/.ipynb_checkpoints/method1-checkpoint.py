#lil-csr-hdd

import numpy as np
from scipy.sparse import bsr_matrix, csr_matrix, lil_matrix, save_npz, load_npz

dense_a = np.zeros([10,10],dtype=np.int8)
lil_a = lil_matrix(dense_a)
lil_a[2,2] = 1
csr_a = lil_a.tocsr()
save_npz('sparse_matrix.npz', csr_a)
csr_a = load_npz('/tmp/sparse_matrix.npz')
print(csr_a.todense())
lil_a = csr_a.tolil()
lil_a[3,3] = 1
csr_a = lil_a.tocsr()
save_npz('sparse_matrix.npz', csr_a)
csr_a = load_npz('sparse_matrix.npz')
print(csr_a.todense())

