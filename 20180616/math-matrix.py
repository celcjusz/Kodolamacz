import numpy as np

def matrix_multiplication(A, B):
    """
    >>> A = [[1, 0], [0, 1]]
    >>> B = [[4, 1], [2, 2]]
    >>> matrix_multiplication(A, B)
    array([[4, 1],
           [2, 2]])
    """
    #reczne mnożenie macierzy najpierw se przypomnieć....

    return np.array(A) @ np.array(B)