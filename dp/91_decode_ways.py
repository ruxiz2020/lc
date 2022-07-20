
class Solution:
    def numDecodings(self, s: str) -> int:
        # Memoization
        dp = { len(s) : 1 }
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if (i + 1 < len(s) and (s[i] == "1" or
                s[i] == "2" and s[i + 1] in "0123456")):
                res += dfs(i + 2)
            dp[i] = res
            return res
        return dfs(0)

        # Dynamic Programming
        dp = { len(s) : 1 }
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if (i + 1 < len(s) and (s[i] == "1" or
                 s[i] == "2" and s[i + 1] in "0123456")):
                dp[i] += dp[i + 2]
        return dp[0]


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
If the last digit is not ‘0’, then there are at least dp[i-1] ways. Based on the pattern above. This is first identification.

Now, we check last two digits. If the last two digit is in greater than ‘09’ and smaller than ‘27’, based on the above pattern, we will add the total ways of step before the last step.

        """
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(dp)):

            if int(s[i-1]) != 0:
                dp[i] = dp[i-1]
            if i != 1 and '09' < s[i-2:i] < '27':
                dp[i] += dp[i-2]

            print(dp)
        return dp[-1]

if __name__ == '__main__':

    s = "226"
    #s = "06"

    ss = Solution()
    res = ss.numDecodings(s)
    print(res)
