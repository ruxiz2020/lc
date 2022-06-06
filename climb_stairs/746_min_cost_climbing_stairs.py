

class Solution(object):
    def minCostClimbingStairs(self, cost):

        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])
        return min(cost[-2], cost[-1])


if __name__ == '__main__':

    cost = [10, 15]

    ss = Solution()
    res = ss.minCostClimbingStairs(cost)

    print(res)
