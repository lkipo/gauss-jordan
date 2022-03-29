from random import gauss
import numpy as np
from pyparsing import col
#from sympy import false

def print_matrix(mat_left, mat_right):

    for i in range(mat_left.shape[0]):
        print("[", end='')
        for j in range(mat_left.shape[1]-1):
            print("{0:.2f}".format(mat_left.item(i * len(mat_left) + j)), end='\t')
        print("{0:.2f}".format(mat_left.item(i * len(mat_left) + mat_left.shape[1]-1)), end='')
        print("]", end='\t')

        print("[", end='')
        for j in range(mat_right.shape[1]-1):
            print("{0:.2f}".format(mat_right.item(i * len(mat_right) + j)), end='\t')
        print("{0:.2f}".format(mat_right.item(i * len(mat_right) + mat_right.shape[1]-1)), end='')
        print("]")

    print()

def gauss_jordan(matrix, amp):
    
    # Obter información da matriz
    filas, columnas = matrix.shape

    #identidade = np.identity(min(columnas, filas))
    
    # triangulacion superior

    for n in range(filas):
        if (matrix[n, n] == 0.0):
            pass
        else:
            if (matrix[n, n] != 1):
                amp[n] = amp[n]/matrix[n, n]
                matrix[n] = matrix[n]/matrix[n, n]
                print_matrix(matrix, amp)

            for i in range(n+1, columnas):
                amp[i] = amp[i] - amp[n] * matrix[i, n]
                matrix[i] = matrix[i] - matrix[n] * matrix[i, n]
                print_matrix(matrix, amp)
    
    # Diagonalización

    for n in range(filas)[::-1]:
        for i in range(1, n+1):
            amp[n-i] = amp[n-i] - amp[n] * matrix[n-i, n]
            matrix[n-i] = matrix[n-i] - matrix[n] * matrix[n-i, n]
            print_matrix(matrix, amp)
        

if __name__=='__main__':
    matriz = np.matrix([[1., 3., 2.], [3., 1., 6.], [7., 2., 9.]])
    identidade = np.matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]])
    print(matriz, '\n')
    inv = np.linalg.inv(matriz)
    gauss_jordan(matriz, identidade)
