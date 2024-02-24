
class Solution:
    def wordBreak(self, s, wordDict):
        L = len(s)
        dp = [False] * (L + 1)
        dp[0] = True
        for i in range(1, L + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    print(s[j:i])
                    dp[i] = True
        print(dp)
        return dp[-1]

class Solution:
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]


if __name__ == '__main__':

    s = "leetcode"
    wordDict = ["leet", "code"]

    ss = Solution()
    res = ss.wordBreak(s, wordDict)
    print(res)
