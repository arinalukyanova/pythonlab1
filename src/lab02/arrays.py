def min_max(nums:list[int|float])-> tuple[int|float,int|float]:
    if len(nums)==0:
        raise ValueError("передан пустой массив")
    else:
        return (min(nums),max(nums))
nums=[1.5, 2, 2.0, -3.1]
print(min_max(nums))
#print(min_max(list(map(float,input().split()))))

#def unique_sorted(nums: list[float | int]) -> list[float | int]:
    #return list(set(nums))
#print(unique_sorted(list(map(float,input().split()))))

#def flatten(mat: list[list | tuple]) -> list:
    #res=list()
    #for n in mat:
        #if type(n) != type([]) and type(n) != type(()):
            #raise TypeError("строка не строка строки матрицы")
        #for i in n:
            #res.append(i)
    #return res
#mat=[[1, 2], "ab"]
#print(flatten(mat))