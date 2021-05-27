# -*- coding: utf-8 -*-
#Lista 10

#3) Faça um programa que gere a seguinte matriz:

# 1 2 3 4 3 2 1
# 2 3 4 5 4 3 2
# 3 4 5 6 5 4 3
# 3 4 5 6 5 4 3
# 2 3 4 5 4 3 2
# 1 2 3 4 3 2 1

import numpy as np

A = np.zeros([6,7])
cont = 0
cont2 = 1

for i in range(0,6):
    if i == 1 or i == 2:
        cont = cont+i  
    for j in range(0,7):      
        A[i,j] = 1 + cont
        if j >= 3:
            if cont != 0:
                cont = cont-1
        else:
            cont = cont+1
    if i >= 3:
        A[i,:] = A[i-cont2,:]
        cont2 = cont2+2
    
        
print(A)