class Solution:
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        m log(sum_)
        Binary search
        n * log(S)
        """
        def canSplit(largest):
            subarray = 0
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > largest:
                    subarray += 1
                    curSum = n
            return subarray + 1 <= m

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = l + ((r - 1) // 2)
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1



