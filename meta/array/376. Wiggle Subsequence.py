import itertools


class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        increasing = 1
        decreasing = 1

        pairs = list(zip(nums[:-1], nums[1:]))
        for a, b in pairs:
            if b > a:
                increasing = decreasing + 1
            elif b < a:
                decreasing = increasing + 1

        return max(increasing, decreasing)


nums = [1,7,4,9,2,5]
res = Solution().wiggleMaxLength(nums)
print(res)
