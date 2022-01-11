class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        chunks = 0
        pre_max = 0
        for i, num in enumerate(arr):
            if num > pre_max:
                pre_max = num
            if pre_max == i:
                chunks += 1
        return chunks
