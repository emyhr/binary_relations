
import numpy as np


def CompleteCheck(matrix):
    """
    CompleteCheck functions tests
    if a binary relations is complete.
    Parameters: matrix representation
    of a binary relation.
    """

    n, m = np.shape(matrix)

    assert n == m, "the input must be a square matrix"

    for i in range(n):
        for j in range(i, n):
            if (not matrix[i][j]) and (not matrix[j][i]):
                return False

    return True


def ReflexiveCheck(matrix):
    """
    ReflexiveCheck functions tests
    if a binary relations is reflexive.
    Parameters: matrix representation
    of a binary relation.
    """

    n, m = np.shape(matrix)

    assert n == m, "the input must be a square matrix"

    for i in range(n):
        if not matrix[i][i]:
            return False

    return True


def AsymmetricCheck(matrix):
    """
    AsymmetricCheck functions tests
    if a binary relations is asymmetric.
    Parameters: matrix representation
    of a binary relation.
    """

    n, m = np.shape(matrix)

    assert n == m, "the input must be a square matrix"

    for i in range(n):
        for j in range(i, n):
            if (not matrix[i][j]) or (not matrix[j][i]):
                return False

    return True


def SymmetricCheck(matrix):
    """
    SymmetricCheck functions tests
    if a binary relations is symmetric.
    Parameters: matrix representation
    of a binary relation.
    """

    n, m = np.shape(matrix)

    assert n == m, "the input must be a square matrix"

    for i in range(n):
        for j in range(m):
            if not (matrix[i][j] == matrix[j][i]):
                return False

    return True

def AntisymmetricCheck(matrix):
    """
    SymmetricCheck functions tests
    if a binary relations is symmetric.
    Parameters: matrix representation
    of a binary relation.
    """
    
    n, m = np.shape(matrix)
    
    assert n == m, "the input must be a square matrix"
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] and matrix[j][i] and (not matrix[i][j] == matrix[j][i]):
                return False
    
    return True


def TransitiveCheck(matrix):
    """
    TransitiveCheck functions tests
    if a binary relations is transitive.
    Parameters: matrix representation
    of a binary relation.
    """

    n, m = np.shape(matrix)

    assert n == m, "the input must be a square matrix"

    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                for k in range(n):
                    if matrix[j][k] and (not matrix[i][k]):
                        return False

    return True


def NegativetransitiveCheck(matrix):
    """
    NegativetransitiveCheck functions tests
    if a binary relations is negative-transitive.
    Parameters: matrix representation
    of a binary relation
    """

    n, m = np.shape(matrix)

    assert n == m, "the input must be a square matrix"

    for i in range(n):
        for j in range(n):
            if not matrix[i][j]:
                for k in range(n):
                    if (not matrix[j][k]) and matrix[i][k]:
                        return False

    return True


def CompleteorderCheck(matrix):
    """
    CompleteorderCheck functions tests
    if a binary relations is a complete order.
    Parameters: matrix representation
    of a binary relation.
    """

    n, m = np.shape(matrix)

    assert n == m, "the input must be a square matrix"

    if CompleteCheck(matrix) and AntisymmetricCheck(matrix) and TransitiveCheck(matrix):
        return True
    else:
        return False

def CompletepreorderCheck(matrix):
        """
        CompletepreorderCheck functions tests
        if a binary relations is a complete preorder.
        Parameters: matrix representation
        of a binary relation
        """

        n, m = np.shape(matrix)

        assert n == m, "the input must be a square matrix"

        if CompleteCheck(matrix) and TransitiveCheck(matrix):
            return True
        else:
            return False


def IndifferenceRelation(matrix):
    """
    IndifferenceRelation function returns
    the indifference relation part of
    a binary relation.
    Parameters: matrix representation
    of a binary relation.
    """

    n, m = np.shape(matrix)

    assert n == m, "the input must be a square matrix"

    sym_elements = []

    for i in range(n):
        for j in range(i, n):
            if matrix[i][j] == matrix[j][i]:
                sym_elements.append((i, j, matrix[i][j]))

    I_matrix = np.zeros((n, n))

    for (i, j, val) in sym_elements:
        I_matrix[i][j] = val
        I_matrix[j][i] = val

    return I_matrix


def StrictRelation(matrix):
    """
    StrictRelation function returns
    the strict relation part of
    a binary relation.
    Parameters: matrix representation
    of a binary relation.
    """

    n, m = np.shape(matrix)

    assert n == m, "the input must be a square matrix"

    asym_elements = []

    for i in range(n):
        for j in range(i, m):
            if matrix[i][j] + matrix[j][i] <= 1:
                asym_elements.append((i, j, matrix[i][j], matrix[j][i]))

    P_matrix = np.zeros((n, n))

    for (i, j, val1, val2) in asym_elements:
        P_matrix[i][j] = val1
        P_matrix[j][i] = val2

    return P_matrix