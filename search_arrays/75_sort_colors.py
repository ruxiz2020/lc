from collections import Counter


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        bucket sort
        O(n)
        """
        count = Counter(nums)
        for i in range(len(nums)):
            if i < count[0]:
                nums[i] = 0
            elif i < count[0] + count[1]:
                nums[i] = 1
            else:
                nums[i] = 2

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        Time complexity : O(nlogn) 
        """
        zero = 0
        two = len(nums) - 1
        i = 0
        while i <= two:
            if nums[i] == 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                i += 1
                zero += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[two], nums[i] = nums[i], nums[two]
                two -= 1
