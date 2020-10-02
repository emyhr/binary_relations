from birel import properties, matrixrel, drawrel, topsort

fpath = "path to your file"


def main():
	matrix = matrixrel.GetMatrix(fpath)
    if properties.AsymmetricCheck(matrix):
        print("Given binary relation is asymmetric")
    drawrel.DrawGraph(matrix).render("graph")
    sorted_graph = topsort.TopSort(matrix)
    print("Topologically sorted graph: ", sorted_graph)


if __name__ == '__main__':
	main()

