from collections import deque
from math import inf
from typing import List


class Solution:
    """
    O(B * M * N)
    O(M * N)
    """
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        que = deque()
        total = 0 # total building count
        # cnt: how many buildings can reach (x,y)
        #      if there is a column all blockers, then (x,y) cannot reach every building
        cnt = [[0] * n for _ in range(m)]
        dist = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    total += 1
                    que.append((i, j))
                    di = 0
                    vis = set() # reset for every free-land
                    while que:
                        di += 1
                        for _ in range(len(que)):
                            r, c = que.popleft()
                            for a, b in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                                x, y = r + a, c + b
                                if (
                                    0 <= x < m
                                    and 0 <= y < n
                                    and grid[x][y] == 0
                                    and (x, y) not in vis
                                ):
                                    cnt[x][y] += 1
                                    dist[x][y] += di
                                    que.append((x, y))
                                    vis.add((x, y))
        print(dist)#[[0, 9, 0, 9, 0], [9, 8, 7, 8, 9], [10, 9, 0, 9, 10]]
        print(cnt)#[[0, 3, 0, 3, 0], [3, 3, 3, 3, 3], [3, 3, 0, 3, 3]]
        ans = inf
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and cnt[i][j] == total:
                    ans = min(ans, dist[i][j])
        return -1 if ans == inf else ans


grid = [[1,0,2,0,1],
        [0,0,0,0,0],
        [0,0,1,0,0]]
ss = Solution()

res = ss.shortestDistance(grid)
print(res) # 7, (1,2)
