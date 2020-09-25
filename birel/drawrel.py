from graphviz import Digraph
import numpy as np

def DrawGraph(matrix):
    """
    DrawGraph function returns
    a graphical representation
    of a binary relation
    Parameters: matrix representation
    of a binary relation.
    """

    n, m = np.shape(matrix)
    assert n == m, "the input must be a square matrix"

    graph = Digraph(name='Indifference part of the binary relation', format='svg')
    edges = np.array(np.nonzero(matrix)).transpose()
    for edge in edges:
        graph.edge(str(edge[0]), str(edge[1]))

    return graph