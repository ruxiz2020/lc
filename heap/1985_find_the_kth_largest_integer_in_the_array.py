import heapq
from typing import List


class Solution:
    # Similar to 215. Kth Largest Element in an Array
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        maxHeap = [-int(n) for n in nums]
        heapq.heapify(maxHeap)

        while k > 1:
            heapq.heappop(maxHeap)
            k -= 1
        print(maxHeap)
        return str(-maxHeap[0])


nums = ["3","6","7","10","12","15"]; k = 4
ss = Solution()
res = ss.kthLargestNumber(nums, k)
print(res)
