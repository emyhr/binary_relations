import pandas as pd


def GetMatrix(fpath):
    """
    GetMatrix function returns
    matrix representation of
    a binary relation.
    Parameters: path to .xls or .csv file.
    """

    ftype = fpath.split('.')[-1]

    assert ftype in ['xls', 'csv'], 'file must either a csv or xls'

    if ftype == 'xls':
        matrix = pd.read_excel(fpath, sep=',', index_col=None, header=None).values
    elif ftype == 'csv':
        matrix = pd.read_csv(fpath, sep=',', index_col=None, header=None).values

    return matrix
