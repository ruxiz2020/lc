import heapq
class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        heap = []
        for i, cost in enumerate(costs):
            heapq.heappush(heap, (cost[1] - cost[0], i))

        res = 0
        count = 0
        while heap:
            cost, pos = heapq.heappop(heap)
            print(cost, pos)
            if count < len(costs) / 2:
                res += costs[pos][1]
            else:
                res += costs[pos][0]
            count += 1
        return res


if __name__ == '__main__':

    costs = [[10,20],[30,200],[400,50],[30,20]]

    ss = Solution()
    res = ss.twoCitySchedCost(costs)

    print(res)
