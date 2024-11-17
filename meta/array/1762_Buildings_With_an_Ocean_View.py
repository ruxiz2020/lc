from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = []
        mx = 0
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > mx:
                ans.append(i)
                mx = heights[i]
        return ans[::-1]


heights = [4,2,3,1]
res = Solution().findBuildings(heights)
print(res) # [0, 2, 3]
