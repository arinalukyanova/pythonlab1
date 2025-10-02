def transpose(mat: list[list[float | int]]) -> list[list]:
    if len(mat)>0 and any(len(row)!=len(mat[0]) for row in mat):
        raise ValueError('Рванная матрица')
    return[list(row) for row in zip(*mat)]
mat=[[1, 2], [3, 4]]
print(transpose(mat))
    