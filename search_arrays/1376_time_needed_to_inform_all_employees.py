class Solution:
  def numOfMinutes(self, n, headID, manager, informTime):
    cache = [-1] * n
    def dfs(cur):
      if cur == -1: return 0
      if cache[cur] == -1:
        cache[cur] = dfs(manager[cur]) + informTime[cur]
      print(cache)
      return cache[cur]
    return max([dfs(i) for i in range(n)])



if __name__ == '__main__':

    n = 6
    headID = 2
    manager = [2,2,-1,2,2,2]
    informTime = [0,0,1,0,0,0]

    n = 7; headID = 6; manager = [1,2,3,4,5,6,-1]; informTime = [0,6,5,4,3,2,1]

    ss = Solution()
    res = ss.numOfMinutes(n, headID, manager, informTime)

    print(res)
