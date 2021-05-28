nums = [11, 2, 7, 11, 15]
target = 9


def two_sum(nums, target):
    seen = {}
    for i, v in enumerate(nums):
        remaining = target - v
        if remaining in seen:
            return [seen[remaining], i]
        seen[v] = i
    return []

rez = two_sum(nums, target)
pass

