class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k <= 0 or not prices:
            return 0
        N = len(prices)
        # 如果k>=N的时候相当于没有限制，题目退化成了不限次数的交易，所以我们直接求今天比昨天高的部分即可。
        if k >= N:
            _sum = 0
            for i in range(1, N):
                if prices[i] > prices[i - 1]:
                    _sum += prices[i] - prices[i - 1]
            return _sum

        #当k<N的时候，我们仍然使用两个变量，全局的收益g和当前天卖出股票的收益l.
        #这里我们需要两个递推公式来分别更新两个变量local和global，参见网友Code Ganker的博客，
        #其中局部最优值是比较前一天并少交易一次的全局最优加上大于0的差值，和前一天的局部最优加上差值后相比，
        #两者之中取较大值，而全局最优比较局部最优和前一天的全局最优。
        #local[i][j] = max(global[i - 1][j - 1] + max(diff, 0), local[i - 1][j] + diff)
        #global[i][j] = max(local[i][j], global[i - 1][j])，
        global_ = [0] * (k + 1)
        local_ = [0] * (k + 1)
        for i in range(N - 1):
            diff = prices[i + 1] - prices[i]
            for j in range(k, 0, -1):
                local_[j] = max(global_[j - 1] + max(diff, 0), local_[j] + diff)
                global_[j] = max(local_[j], global_[j])
        return global_[-1]
