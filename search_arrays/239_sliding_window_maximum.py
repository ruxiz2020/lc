import collections
from typing import List

class Solution:
    '''monotonic decreasing order queue'''
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        indexQ = collections.deque()
        valQ = collections.deque()

        res = []
        for i, n in enumerate(nums):
            while valQ and n > valQ[-1]:
                valQ.pop()
                indexQ.pop()
            valQ.append(n)
            indexQ.append(i)

            while i - indexQ[0] + 1 > k:
                valQ.popleft()
                indexQ.popleft()
            if i + 1 >= k:
                res.append(valQ[0])
        return res



if __name__ == '__main__':

    nums = [1,3,-1,-3,5,3,6,7]
    k = 3

    ss = Solution()
    res = ss.maxSlidingWindow(nums, k)

    print(res)
