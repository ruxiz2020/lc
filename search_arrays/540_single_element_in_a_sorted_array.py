from functools import reduce


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x ^ y, nums)


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + ((l - r) // 2)  # to avoid overflow
            if ((m - 1 < 0 or nums[m - 1] != nums[m]) and
                    (m + 1 == len(nums) or nums[m] != nums[m + 1])):
                return nums[m]

            leftSize = m - 1 if nums[m - 1] == nums[m] else m
            if leftSize % 2:
                r = m - 1
            else:
                l = m + 1

