class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        N = len(cost)
        cost.append(0)
        dp = [0] * (N + 1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, N + 1):

            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
            print(i)
        #print(dp)
        return dp[-1]


if __name__ == '__main__':

    cost = [10,15,20]
    ss = Solution()
    res = ss.minCostClimbingStairs(cost)

    print(res)
