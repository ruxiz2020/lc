import collections
from typing import List


class Solution:
    '''monotonic decreasing order queue
    This code finds the maximum value within each sliding window of size 
    k in an array by keeping a monotonic decreasing deque, where smaller 
    elements are removed from the back to maintain descending order.

    The element at the front of the deque is the largest in the current window, 
    and any index that falls out of the window’s range is removed from the front.
    
    The time complexity is 
    O(n) because each element is pushed and popped from the deque at most once, 
    and the space complexity is O(k) for storing up to k elements in the deque.
    O(N)
    O(k)'''

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
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    ss = Solution()
    res = ss.maxSlidingWindow(nums, k)

    print(res)  # [3, 3, 5, 5, 6, 7]
