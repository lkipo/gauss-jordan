import numpy as np
import pandas as pd

def print_matrix(mat_left, mat_right):
    a = []
    for i in range(len(mat_left)):
        a.append('|')
    df = pd.DataFrame(mat_left)
    df2 = pd.concat([df, pd.DataFrame(['|', '|', '|']), pd.DataFrame(mat_right)], axis=1)
    print(df2)
    print('\n')

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
    ter_ind = np.matrix([[1.], [2.], [6.]])
    print_matrix(matriz, ter_ind)
    inv = np.linalg.inv(matriz)
    gauss_jordan(matriz, ter_ind)