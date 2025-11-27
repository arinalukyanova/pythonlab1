def min_max(nums: list[int | float]) -> tuple[int | float, int | float]:
    if len(nums) == 0:
        raise ValueError("передан пустой массив")
    else:
        return (min(nums), max(nums))


nums = [1.5, 2, 2.0, -3.1]
print(min_max(nums))
# print(min_max(list(map(float,input().split()))))
