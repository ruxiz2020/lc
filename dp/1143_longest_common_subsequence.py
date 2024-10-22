class Solution:
  def longestCommonSubsequence(self, text1, text2):
    m = len(text1)
    n = len(text2)
    # dp[i][j] := LCS's length of text1[0..i) and text2[0..j)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if text1[i] ==  text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

    return dp[0][0]


if __name__ == '__main__':

    text1 = "abcde"
    text2 = "ace"

    ss = Solution()
    res = ss.longestCommonSubsequence(text1, text2)
    print(res)
