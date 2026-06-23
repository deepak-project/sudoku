import numpy as np

def sudoku_slover(a):
    for i in range(9):
        rows = a[[i], : ]

        if np.sum(rows == 0) == 1 :
            for j in range(9):
                if np.sum(rows == j) == 1:
                    rows[rows == 0] == j
            
    for i in range(9):
        coul = a[ :, [i]]

        if np.sum(coul == 0) == 1 :
            for j in range(9):
                if np.sum(coul == j) == 1:
                    coul[coul == 0] == j
