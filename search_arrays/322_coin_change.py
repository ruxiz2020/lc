class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        bottom up
        O(nm)
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                #print('coin', 'i')
                #print(coin, i)
                if dp[i - coin] != float('inf'):
                    #print(dp[i], dp[i - coin] + 1)
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    #print('dp[i]')
                    print(coin)
                    print(dp)
        return -1 if dp[amount] == float('inf') else dp[amount]


if __name__ == '__main__':

    coins = [1,2,5]; amount = 11
    #coins = [2]; amount = 3

    ss = Solution()
    res = ss.coinChange(coins, amount)

    print(res)
