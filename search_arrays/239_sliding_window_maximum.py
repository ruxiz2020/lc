import collections

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        a deque that is always decreasing 
        O(n)
        """
        que = collections.deque() # [[i, num]]
        res = []
        for i, num in enumerate(nums):
            print(que)
            if que and i - que[0][0] >= k:
                que.popleft()
            while que and que[-1][1] <= num:
                que.pop()
            que.append([i, num])
            if i >= k - 1:
                res.append(que[0][1])
        return res



if __name__ == '__main__':

    nums = [1,3,-1,-3,5,3,6,7]
    k = 3

    ss = Solution()
    res = ss.maxSlidingWindow(nums, k)

    print(res)
