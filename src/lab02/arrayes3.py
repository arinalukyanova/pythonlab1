def flatten(mat: list[list | tuple]) -> list:
    res = list()
    for n in mat:
        if type(n) != type([]) and type(n) != type(()):
            raise TypeError("строка не строка строки матрицы")
        for i in n:
            res.append(i)
    return res


mat = [[1], [], [2, 3]]
print(flatten(mat))
