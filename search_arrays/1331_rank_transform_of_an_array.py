class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        tmp = list(set(arr))
        tmp.sort()
        print(tmp)
        d = {c:i + 1 for i, c in enumerate(tmp)}
        return [d[c] for c in arr]

