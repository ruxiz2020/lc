class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        sell = [0] * len(prices)
        hold = [0] * len(prices)
        hold[0] = -prices[0]
        for i in range(1, len(prices)):
            sell[i] = max(sell[i - 1], hold[i - 1] + prices[i])
            hold[i] = max(hold[i - 1], (sell[i - 2] if i >= 2 else 0) - prices[i])
        return sell[-1]


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = {}  #key=(i, buying) val=max_profit
        def dfs(i, buying):
            if i >=len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            if buying:
                buy = dfs(i + 1, False) - prices[i]
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, True) + prices[i]
                cooldown = dfs(i + 1, buying)
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(sell, cooldown)
            print(dp)
            return dp[(i, buying)]
        return dfs(0, True)


if __name__ == '__main__':

    prices = [1,2,3,0,2]

    ss = Solution()
    res = ss.maxProfit(prices)

    print(res)
