class Solution:
    def wordBreak(self, s, wordDict):
        """
        O( N^2 * M), m: avg words length in wordDict
        O(N)
        """
        L = len(s)
        dp = [False] * (L + 1)
        dp[0] = True
        for i in range(1, L + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    print(s[j:i])
                    dp[i] = True
        print(dp)  # [True, False, False, False, True, False, False, False, True]
        return dp[-1]


if __name__ == '__main__':
    s = "leetcode"
    wordDict = ["leet", "code"]

    ss = Solution()
    res = ss.wordBreak(s, wordDict)
    print(res)
