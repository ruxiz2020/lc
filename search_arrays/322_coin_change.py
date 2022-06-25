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


class Solution:
    '''bottom up'''
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1



if __name__ == '__main__':

    coins = [1,2,5]; amount = 11
    #coins = [2]; amount = 3

    ss = Solution()
    res = ss.coinChange(coins, amount)

    print(res)
