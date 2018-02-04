import numpy as np

def matrix_gen(n,k):
    return np.random.randint(2, size=(n, k)).tolist()

def one_man_transform(mat):
    h , w = np.matrix(mat).shape
    d = {}
    for i in range(int(h)):
        for j in range(int(w)):
            if mat[i][j] == 1:
                d[i]=j
    for k,v in d.items():
        if not k+1 >= h:
            mat[k+1][v] = 1
        if not 1+v >= w:
            mat[k][1+v] = 1
        if not k-1 < 0:
            mat[k-1][v] = 1
        if not v-1 < 0:
            mat[k][v-1] = 1
    return mat

def n_man_transfrom(mat,n):
    h , w = np.matrix(mat).shape
    d = {}
    for i in range(int(h)):
        for j in range(int(w)):
            if mat[i][j] == 1:
                d[i]=j
    for k,v in d.items():
        if not k+1 >= h:
            mat[k+1][v] = 1
        if not 1+v >= w:
            mat[k][1+v] = 1
        if not k-1 < 0:
            mat[k-1][v] = 1
        if not v-1 < 0:
            mat[k][v-1] = 1
        
        # n transform top,bottom,left,right   
        if not k+n >= h:
            mat[k+n][v] = 1
        if not v+n >=w:
            mat[k][n+v] = 1
        if not k-n < 0:
            mat[k-n][v] = 1
        if not v-n < 0:
            mat[k][v-n] = 1        
        #n-1 transform diagonals topleft,topright,bottomleft,bottomright
        #bottomright
        if not k+n-1 >= h and not n-1+v >= w:
            mat[k+n-1][v+n-1] = 1
        #topright
        if not n-1+v >= w and not k-n-1 < 0:
            mat[k-n-1][n-1+v] = 1
        #topleft
        if not k-n-1 < 0 and not v-n-1 < 0:
            mat[k-n-1][v-n-1] = 1
        #bottomleft
        if not v-n-1 < 0 and not k+n-1 >= h:
            mat[k+n-1][v-n-1] = 1 

    return mat


               
            
