import numpy as np

def TopSort(matrix):
    """
    TopSort is a function that
    returns a list of topologically
    sorted nodes of a graph.
    Parameters: matrix representation
    of a binary relation.
    """

    n, m = np.shape(matrix)

    assert n == m, "the input must be a square matrix"

    # nodes with no incoming edges
    no_predecessors = list(set(range(n)) - set(np.nonzero(matrix)[1]))
    sorted_nodes = []  # sorted

    assert len(no_predecessors) > 0, "input is not DAG!"

    while no_predecessors:
        sorted_nodes.append(no_predecessors[0])  # sorted
        out_nodes = np.nonzero(matrix[no_predecessors[0]])[0]  # child-nodes of the current node
        del no_predecessors[0]
        for node in out_nodes:
            matrix[sorted_nodes[len(sorted_nodes) - 1]][node] = 0  # removing the current edge
            if not (node in set(np.nonzero(matrix)[1])):
                no_predecessors.append(node)

    if np.array(np.nonzero(matrix)).size == 0:
        return sorted_nodes
    else:
        raise ValueError("Input matrix is not DAG!")

