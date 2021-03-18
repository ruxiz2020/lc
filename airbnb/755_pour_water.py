class Solution(object):
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        for _ in range(V):
            curr = K
            while curr > 0 and heights[curr] >= heights[curr - 1]:
                curr -= 1
            while curr < len(heights) - 1 and heights[curr] >= heights[curr + 1]:
                curr += 1
            while curr > K and heights[curr] >= heights[curr - 1]:
                curr -= 1
            heights[curr] += 1
        return heights
