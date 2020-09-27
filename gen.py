import numpy as np


def CompleteGen(n):
    """
    CompleteGen generates
    matrix representation
    of a complete binary relation
    of given size.
    Parameters: binary relation size
    """

    matrix = np.zeros((n, n))

    for i in range(n):

        matrix[i][i] = 1
        for j in range(i + 1, n):
            matrix[i][j] = np.random.randint(0, 2)
            if not matrix[i][j]:
                matrix[j][i] = 1
            else:
                matrix[j][i] = np.random.randint(0, 2)

    return matrix


def ReflexiveGen(n):
    """
    ReflexiveGen generates
    matrix representation
    of a reflexive binary relation
    of given size.
    Parameters: binary relation size
    """

    matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            matrix[i][j] = 1 if i == j else np.random.randint(0, 2)

    return matrix


def AsymmetricGen(n):
    """
    AsymmetricGen generates
    matrix representation
    of a asymmetric binary relation
    of given size.
    Parameters: binary relation size
    """

    matrix = np.zeros((n, n))

    for i in range(n):
        matrix[i][i] = 0
        for j in range(i + 1, n):
            matrix[i][j] = np.random.randint(0, 2)
            if matrix[i][j]:
                matrix[j][i] = 0
            else:
                matrix[j][i] = np.random.randint(0, 2)

    return matrix


def SymmetricGen(n):
    """
    SymmetricGen generates
    matrix representation
    of a symmetric binary relation
    of given size.
    Parameters: binary relation size
    """

    matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(i, n):
            matrix[i][j] = np.random.randint(0, 2)
            matrix[j][i] = matrix[i][j]

    return matrix
