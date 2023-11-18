class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        T: O(n ^ 2)
        S: O(n ^ 2)
        numTree[4] = numTree[0] * numTree[3] + (node 0 as the root)
                     numTree[1] * numTree[2] + (node 1 as the root)
                     numTree[2] * numTree[1] + (node 2 as the root)
                     numTree[3] * numTree[0] (node 3 as the root)
        """
        dp = {0:1, 1:1, 2:2}
        if n < 3: return dp[n]
        for i in range(3, n+1):
            num = 0
            for j in range(i):
                num += dp[j]*dp[i-j-1]
            dp[i] = num
        return dp[n]
