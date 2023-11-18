from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Keep track of visited number and its index position. E.g. {2:0}
        visited = {}
        numsLen = len(nums)
        for currIdx in range(numsLen):
            currNum = nums[currIdx]
            remaining = target - currNum
            # Did we already visit a number that the current number can add up to the target?
            if remaining in visited:
                visitedIdx = visited[remaining]
                return [visitedIdx, currIdx]
            else:
                visited[currNum] = currIdx
