import heapq
from typing import List

class Solution:
  def smallestRange(self, nums: List[List[int]]) -> List[int]:
    minHeap = [(row[0], i, 0) for i, row in enumerate(nums)]
    heapq.heapify(minHeap)
    print(minHeap)

    maxRange = max(row[0] for row in nums)
    minRange = heapq.nsmallest(1, minHeap)[0][0]
    ans = [minRange, maxRange]
    print(ans)

    while len(minHeap) == len(nums):
        # pop and push from the same row
        num, r, c = heapq.heappop(minHeap) # lower boundary at this moment
        if c + 1 < len(nums[r]):
            heapq.heappush(minHeap, (nums[r][c + 1], r, c + 1))
            maxRange = max(maxRange, nums[r][c + 1]) # update upper bound
            minRange = heapq.nsmallest(1, minHeap)[0][0] # update lower bound
            if maxRange - minRange < ans[1] - ans[0]:
                ans[0], ans[1] = minRange, maxRange

    return ans


if __name__ == '__main__':

    nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]

    ss = Solution()
    res = ss.smallestRange(nums)

    print(res)
