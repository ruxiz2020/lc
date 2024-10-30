class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        return len(s) - self._longestPalindromeSubseq(s) <= k

    # Same as 516. Longest Palindromic Subsequence
    def _longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # dp[i][j] := the length of LPS(s[i..j])
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for d in range(1, n):
            for i in range(n - d):
                j = i + d
                print(i, j)
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]


s = "abcdeca"; k = 2

"""
0 (1) 2 3 4 5
1 1 (2)    (last)
2   1 (3)
3     1
4       1
5         1
"""

ss = Solution()
res = ss.isValidPalindrome(s, k)
print(res)
