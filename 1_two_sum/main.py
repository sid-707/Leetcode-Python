def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}

    for i, num in enumerate(nums):
        difference = target - num
        if difference in seen:
            return [seen[difference], i]

        seen[num] = i
