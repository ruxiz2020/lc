class Solution:
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        # base case
        if k == 0: return []
        win = sorted(nums[:k])
        ans = []
        for i in range(k, len(nums)+1):
            median = (win[k//2] + win[(k-1)//2])/2.0
            ans.append(median)
            if i == len(nums):
                break
            # get the index of the nums[i-k] and then delete it, then insort nums[i]
            index = bisect.bisect_left(win, nums[i-k])
            win.pop(index)
            bisect.insort_left(win, nums[i])

        return ans
