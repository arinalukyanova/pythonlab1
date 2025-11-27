def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    kol_simv_in_first = len(mat[0])
    for row in mat:
        if len(row) != kol_simv_in_first:
            raise ValueError("Матрица не прямоугольная")
    sums = [0] * kol_simv_in_first
    for row in mat:
        for i in range(kol_simv_in_first):
            sums[i] += row[i]
    return sums


mat = [[-1, 1], [10, -10]]
print(col_sums(mat))
