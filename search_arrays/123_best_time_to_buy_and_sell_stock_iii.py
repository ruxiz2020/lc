class Solution:
    def maxProfit(self, prices):
        sell1 = sell2 = 0
        buy1 = buy2 = -float('inf')
        for p in prices:
            buy1 = max(buy1, -p);
            sell1 = max(sell1, buy1 + p)
            buy2 = max(buy2, sell1 - p)
            sell2 = max(sell2, buy2 + p)
        return sell2
