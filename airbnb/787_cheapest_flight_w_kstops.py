class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        f = collections.defaultdict(dict)
        for u, v, w in flights:
            f[u][v] = w
        # q saves the price to current city, current city, and the remaing steps
        q = [(0, src, K+1)]
        while q:
            price, curr, step = heapq.heappop(q)
            if curr == dst:
                return price
            if step > 0:
                for next in f[curr]:
                    heapq.heappush(q, (price + f[curr][next], next, step-1))
        return -1
