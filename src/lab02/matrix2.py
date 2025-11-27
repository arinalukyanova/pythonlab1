def row_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat) > 0 and any(len(row) != len(mat[0]) for row in mat):
        raise ValueError("Рванная матрица")
    sums = [sum(row) for row in mat]
    return sums


mat = [[1, 2, 3], [4, 5, 6]]
print(row_sums(mat))
