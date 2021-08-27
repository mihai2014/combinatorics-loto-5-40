#lil-pickle-hdd

import numpy as np
from scipy.sparse import lil_matrix
import pickle

dense_a = np.zeros([10,10],dtype=np.int8)
lil_a = lil_matrix(dense_a)
lil_a[2,2] = 1
#print(lil_a.todense())

pickle_bin = pickle.dumps(lil_a)
f = open("data_c5.bin", mode = 'wb')
f.write(pickle_bin)
f.close()

f = open('data_c5.bin', 'rb')
pickle_bin = f.read()
f.close()
lil_a = pickle.loads(pickle_bin)
print(lil_a.todense())



#  pickle.dump(obj, file, protocol=None, *, fix_imports=True, buffer_callback=None)
#  pickle.dumps(obj, protocol=None, *, fix_imports=True, buffer_callback=None)
#  pickle.load(file, *, fix_imports=True, encoding="ASCII", errors="strict", buffers=None)
#  pickle.loads(bytes_object, *, fix_imports=True, encoding="ASCII", errors="strict", buffers=None)

