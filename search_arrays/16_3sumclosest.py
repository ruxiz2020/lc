class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N = len(nums)
        nums.sort()
        res = float('inf') # sum of 3 number
        for t in range(N):
            i, j = t + 1, N - 1
            while i < j:
                _sum = nums[t] + nums[i] + nums[j]
                if abs(_sum - target) < abs(res - target):
                    res = _sum
                if _sum > target:
                    j -= 1
                elif _sum < target:
                    i += 1
                else:
                    return target
        return res
