class Solution:
  def findCheapestPrice(self, n, flights, src, dst, K):
    '''Bellman-Ford'''
    kInfCost = float('inf')
    cost = [kInfCost for _ in range(n)]
    cost[src] = 0

    for i in range(K + 1):

      tmp = list(cost)

      for p in flights:
        tmp[p[1]] = min(tmp[p[1]], cost[p[0]] + p[2])
        #print(tmp[p[1]], cost[p[0]] + p[2])
        #print("cost")
        #print(cost)
        #print("p")
        #print(p)
        #print("tmp")
        #print(tmp)
      cost = tmp

    #print(cost)

    return -1 if cost[dst] >= float('inf') else cost[dst]



if __name__ == '__main__':

    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 1

    ss = Solution()
    res = ss.findCheapestPrice(n, flights, src, dst, k)
    print(res)
