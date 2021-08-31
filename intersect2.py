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
import time

class Reducere():
    def __init__(self, arr):
        self.n = len(arr)
        start = time.time()
        self.c5 = self.comb(arr,5)
        end = time.time()
        print("memory c5 list ready:",len(self.c5))
        print(end - start,"seconds")
        #c5 list #################################
        self.solutions = []
        #index list #################################
        self.solutions2 = []   
        self.nr_crt = 0
        
    def comb(self, arr, k):
        # return list of all subsets of length k
        # to deal with duplicate subsets use 
        # set(list(combinations(arr, k)))
        return list(combinations(arr, k))

    def recover_state(self,m):

        #verify if saved m changed or undefined (no ini files)
        try:
            f = open('data_c5.ini','r')
            m_ini = int(f.read())
            f.close()
            if(m_ini != m):
                os.system("rm data_c5.ini")
                os.system("rm data_c5.bin")
                m_ini = 0    
        except:
            m_ini = 0
                        
        #there is not any m in ini file or m changed
        if(m_ini == 0):
            print("Begin process for m=",m)

            #init list
            self.solutions.append(self.c5[0])
            self.solutions2.append(0)            
            
            f = open('data_c5.ini','w')
            f.write(str(m))
            f.close()        
            
        else:
            print("Recover state. m=",m_ini) 
            
            
        try:
            f = open('data_c5.bin','rb')
            pickle_bin = f.read()
            f.close()
            self.solutions2 = pickle.loads(pickle_bin)
            print("recover state (solutions indexes):", self.solutions2)
            #init self.solutions
            self.solutions = np.array(self.c5)[self.solutions2,:].tolist()
            #convert list item to tuple
            i = 0
            for item in self.solutions:
                self.solutions[i] = tuple(item)
                i+= 1
            #print(self.solutions)
            self.nr_crt = len(self.solutions2)
        except:    
            pass    
    
    def process_intersect(self):     
        
        go = True
        while(go):        
        
            #choose one solution
            i = 0
            for c in self.c5:
                set_c = set(c)

                all_intersections = np.zeros(len(self.solutions))
                j = 0
                for s in self.solutions:            
                    set_s = set(s)
                    intersections = len(set_c & set_s)
                    all_intersections[j] = intersections
                    j += 1    

                if (all_intersections.max() <=2):
                    #print("max",all_intersections.max())
                    go = True
                    self.nr_crt += 1
                    print(self.nr_crt,i)
                    self.solutions.append(self.c5[i])
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

                i += 1   
                
        print("END")    

    def display_matrix(self,m):
        self.recover_state(m)

        nr = 1
        for s in self.solutions:
            print(f"{nr},{s[0]},{s[1]},{s[2]},{s[3]},{s[4]}")
            nr += 1
        #s = np.array(self.solutions)    
        #print("Sums:",s.sum(axis=0))    
        
    def cover(self,m):
        self.recover_state(m)    
                
        start = time.time()
        self.c6 = self.comb(arr,6)
        end = time.time()
        print("memory c6 list ready:",len(self.c6))
        print(end - start,"seconds")        
        
        c6_hit_indexes = []
        for s in self.solutions:
                set_s = set(s)
                index = 0
                for c6 in self.c6:
                    set_c6 = set(c6)
                    intersections = len(set_c6 & set_s)
                    
                    if(intersections >= 4):
                        #print(intersections)
                        c6_hit_indexes.append(index)
                    index += 1     
                    
        #print(c6_hit_indexes)
        hit_c6 = np.array(c6_hit_indexes)
        hit_c6 = np.unique(hit_c6)        
        hit_c6 = hit_c6.shape[0]
        all_c6 = len(self.c6)
        print("Cover - total", hit_c6, hit_c6*100/all_c6,"%")                    
        
        
    def go(self,m):
        self.recover_state(m)
        self.process_intersect()
        self.display_matrix(m)

#select m, execute go(), then comment go and uncomment display_matrix() and/or cover()

m=10
arr = np.arange(start=1, stop=m+1, step=1)
calc = Reducere(arr)
calc.go(m)
#calc.display_matrix(m)
#calc.cover(m)
