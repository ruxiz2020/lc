class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        dp = 0
        res = 0
        prev = -1
        for i, a in enumerate(A):
            if a < L and i > 0:
                res += dp
            elif a > R:
                dp = 0
                prev = i
            elif L <= a <= R:
                dp = i - prev
                res += dp
        return res
