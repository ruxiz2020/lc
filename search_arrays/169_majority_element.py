# O(NlogN)
from collections import Counter
class Solution2(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = Counter(nums)
        for key in counter:
            if counter[key] > len(nums)//2:
                return key


# O(NlogN)
class Solution3(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        mid = len(nums)//2
        return nums[mid]
