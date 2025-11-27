def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return list(set(nums))


nums = [1.0, 1, 2.5, 2.5, 0]
print(unique_sorted(nums))
