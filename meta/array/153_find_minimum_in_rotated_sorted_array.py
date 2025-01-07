class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        O(log N)
        O(1)
        """
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] <= nums[high]:  # min位于左侧上升沿
                high = mid
            else:  # min位于左侧上升沿与右侧上升沿之间
                low = mid + 1
        return nums[low]


# Test the Solution
nums = [4, 5, 6, 7, 0, 1, 2]  # Rotated sorted array
solution = Solution()
result = solution.findMin(nums)
print("Minimum value in the array:", result)  # Expected Output: 0
