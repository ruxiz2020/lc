class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        M, N = len(A), len(A[0])
        for i in range(M):
            if A[i][0] == 0:
                for j in range(N):
                    A[i][j] = 1 - A[i][j]
        res = 0
        for j in range(N):
            count1 = 0
            for i in range(M):
                if A[i][j]:
                    count1 += 1
            res += (1 << N - 1- j) * max(count1, M - count1)
        return res
