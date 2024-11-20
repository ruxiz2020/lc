import random


class Solution:
    def __init__(self, nums: list[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        ans = -1
        rng = 0
        for i, num in enumerate(self.nums):
            if num == target:
                rng += 1
                # print(rng)
                if random.randint(0, rng - 1) == 0:
                    print(rng - 1)
                    ans = i
        return ans

nums = [1, 2, 3, 3, 3]
ss = Solution(nums)

res = ss.pick(3)
print(res)
"""Input
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
Output
[null, 4, 0, 2]"""
