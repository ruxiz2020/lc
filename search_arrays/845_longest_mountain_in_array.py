class Solution:
    def longestMountain(self, A):
        n = len(A)
        res = l = 0
        while l + 2 < n:
            r = l + 1
            if A[l] < A[l + 1]:
                while r + 1 < n and A[r] < A[r + 1]:
                    r += 1
                if r < n - 1 and A[r] > A[r + 1]:
                    while r + 1 < n and A[r] > A[r + 1]:
                        r += 1
                    res = max(res, r - l + 1)
                else:
                    r += 1
            l = r
        return res
