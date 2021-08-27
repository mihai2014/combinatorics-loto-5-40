#        m1                             m2
#Ex: 12......n                       12....n       
# -------------------5-----------------------------6
#    1111100000 |  C    = rows      11111100.. | C
#    1111010000 |   arr             1111101..  |  arr
#    ...        |                   ...        |
#         11111 V                      111111  V
#
# intersect   = m1 X m2.T
#    c6 ---->  (axis=1)
# c5 
# |   5 5 ....
# |   ... 
# v   ..  0 0
#
# (axis=0)

# Function which returns subset or r length from n
from scipy.sparse import csr_matrix, lil_matrix
from itertools import combinations
import numpy as np
import math
import sys
import os
import gc
import time
import pickle

#def delete_row_lil(mat, i):
#    if not isinstance(mat, scipy.sparse.lil_matrix):
#        raise ValueError("works only for LIL format -- use .tolil() first")
#    mat.rows = np.delete(mat.rows, i)
#    mat.data = np.delete(mat.data, i)
#    mat._shape = (mat._shape[0] - 1, mat._shape[1])

class Reducere():
    def __init__(self, arr):
        self.n = len(arr)
        self.m5, self.c5 = self.matrix5(arr)
        print("memory m5 ready:",self.m5.shape)
        dim = self.m5.shape[0]
        #binar list #################################
        self.solutions = []
        #index list #################################
        self.solutions2 = []   
        self.nr_crt = 0
        
    def comb(self, arr, k):
        # return list of all subsets of length k
        # to deal with duplicate subsets use 
        # set(list(combinations(arr, k)))
        return list(combinations(arr, k))

    #"graphical" matrix (0/1 int8)
    def matrix5(self,arr):
        comb = self.comb(arr,5)
        cols = self.n
        rows = math.comb(cols,5)

        #z = np.zeros((rows,cols), dtype = np.int8)
        z = lil_matrix((rows, cols), dtype=np.int8)
        i = 0
        for c in comb:
            
            n1 = c[0]
            n2 = c[1]
            n3 = c[2]
            n4 = c[3]
            n5 = c[4]

            z[i,n1-1] = 1
            z[i,n2-1] = 1
            z[i,n3-1] = 1
            z[i,n4-1] = 1
            z[i,n5-1] = 1
                
            #print(i,z[i])
            i += 1

        return z, comb   
    
    def process_intersect(self):
        dim = self.m5.shape[0]    

        for i in range(dim):
            #print(dim,"<--",i)
            row1 = self.m5[i,:].toarray()[0]    
            for j in range(dim):
                #print(i,j)
                row2 = self.m5[j,:].toarray()[0]    
                result = row1@row2
                #self.fp_intersect[i,j] = result

    def save_state(self):
        pass
        try:
            f = open('data_c5.bin','rb')
            pickle_bin = f.read()
            f.close()
            self.solutions2 = pickle.loads(pickle_bin)
            print("recover state (indexes):", self.solutions2)
            #init self.solutions
            self.solutions = self.m5.toarray()[[self.solutions2],:][0].tolist()
            #print(self.solutions)
            self.nr_crt = len(self.solutions2)
        except:    
            pass
                                   
    def process_intersect2(self):
        dim = self.m5.shape[0]   

        go = True
        while(go):
        
            #choose one solution
            for i in range(dim):
                c = self.m5[i,:].toarray()[0] 

                all_intersections = np.zeros(dim)
                j = 0
                for s in self.solutions:
                    s = np.array(s)
                    intersections = c@s
                    all_intersections[j] = intersections
                    j += 1

                if (all_intersections.max() <=2):
                    go = True
                    self.nr_crt += 1
                    print(self.nr_crt,i)
                    self.solutions.append(self.m5[i,:].toarray()[0].tolist())
                    self.solutions2.append(i)
                    #save state to hdd (overwrite)
                    f = open("data_c5.bin",'wb')
                    f.seek(0)
                    f.write(pickle.dumps(self.solutions2))
                    f.truncate()        
                    f.close()
                    break
                else:
                    go = False
                
        print("END")
           
    def display_matrix(self):
        for s in self.solutions:
            print(s)
        s = np.array(self.solutions)    
        print("Sums:",s.sum(axis=0))

    def cover(self):
        pass

    def interpret(self):
        self.save_state()
        self.display_matrix()
        c5_array = np.array(self.c5)
        solution = c5_array[self.solutions2,:]
        for c in solution:
            print(f"{c[0]},{c[1]},{c[2]},{c[3]},{c[4]}")
        
    
    def go(self):
        self.save_state()
        self.process_intersect2()
        self.display_matrix()
        #print(self.solutions)
                

m=10
arr = np.arange(start=1, stop=m+1, step=1)
calc = Reducere(arr) 
calc.go()
#calc.interpret()
