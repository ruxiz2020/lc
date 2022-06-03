from typing import List


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        """
        Kadane's Algorithm
        Two cases:
        1. normal max subarray within A
        2. circular one, that both A[0] and A[n-1] is included
        (A0 + A1 + .. + Ai) + (Aj + ... + An-1)
        = sum(A) - (Ai+1 + ... + Aj-1)
        """
        ret1 = self.max_subarray(A)
        ret2 = sum(A) + self.max_subarray([-a for a in A[1:-1]])  # max negative (-1)
        return max(ret1, ret2)

    def max_subarray(self, A) -> int:
        """
        dp[i] = A[i] + max(dp[i-1],0)
        """
        mx = -float('inf')
        cur = 0
        for a in A:
            cur = a + max(cur, 0)  # RHS cur is the prev
            mx = max(mx, cur)
        return mx
