class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        O(log(m+n))
        factorial(m + n -2)//(factorial(m - 1) * factorial(n - 1))
        """
        total = m + n - 2
        v = n - 1

        def permutation(m, n):
            son = 1
            for i in range(m, m - n, -1):
                son *= i
            mom = 1
            for i in range(n, 0, -1):
                mom *= i
            return son / mom
        return permutation(total, min(v, total - v))


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        O(n * m) O(n)
        """
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1] 


if __name__ == '__main__':

    m = 3
    n = 7

    ss = Solution()
    res = ss.uniquePaths(m, n)

    print(res)
