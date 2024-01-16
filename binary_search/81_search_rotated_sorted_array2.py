class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        augmented binary search
        """
        N = len(nums)
        l, r = 0, N - 1
        while l <= r:
            # augmented part
            while l < r and nums[l] == nums[r]:
                l += 1
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            if nums[mid] >= nums[l]: # left portion
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] <= nums[r]: # right portion
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
