class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        O（m n)
        """
        len_s1 = len(s1)
        len_s2 = len(s2)
        len_s3 = len(s3)
        if len_s1 + len_s2 != len_s3:
            return False
        dp = [[False for i in range(len_s2 + 1)] for j in range(len_s1 + 1)]
        for i in range(0,len_s1 + 1):
            for j in range(0,len_s2 + 1):

                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j-1] and (s2[j-1] == s3[j-1])
                elif j == 0:
                    dp[i][j] = dp[i-1][j] and (s1[i-1] == s3[i-1])
                else:
                    dp[i][j] = (dp[i-1][j] and s1[i-1] == s3 [i + j - 1]) or \
                                (dp[i][j-1] and s2[j-1]== s3[i+j-1])

        print(dp)
        return dp[len_s1][len_s2]

if __name__ == '__main__':

    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"

    ss = Solution()
    res = ss.isInterleave(s1, s2, s3)
    print(res)
