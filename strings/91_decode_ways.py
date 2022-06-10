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
        return dp[-1]


if __name__ == '__main__':

    s = "226"
    s = "06"

    ss = Solution()
    res = ss.numDecodings(s)
    print(res)
