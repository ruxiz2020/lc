class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        '''Bellman-Ford
        BFS
        O(E * K)'''
        kInfCost = float('inf')
        cost = [kInfCost for _ in range(n)]
        cost[src] = 0

        for i in range(K + 1):

            tmp = list(cost)

            for s, d, p in flights:
                if cost[s] == float("inf"):
                    continue
                if cost[s] + p < cost[d]:
                    tmp[d] = cost[s] + p
            cost = tmp

        return -1 if cost[dst] >= float('inf') else cost[dst]


if __name__ == '__main__':
    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1

    ss = Solution()
    res = ss.findCheapestPrice(n, flights, src, dst, k)
    print(res)
