from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for num in nums:
            if num != 0:
                nums[j] = num
                j += 1

        for i in range(j, len(nums)):
            nums[i] = 0

nums = [0,1,0,3,12]
ss = Solution().moveZeroes(nums)
print(nums)
# [1, 3, 12, 0, 0]
