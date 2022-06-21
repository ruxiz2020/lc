from typing import List
import collections

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(dict)
        for con in connections:
            graph[con[0]][con[1]] = 1
            graph[con[1]][con[0]] = 0

        print(graph)
        visited = set()
        return self.dfs(graph, 0, visited)

    def dfs(self, graph, cur, visited):
        res = 0
        visited.add(cur)
        for nxt, value in graph[cur].items():
            if nxt not in visited:
                res += value
                res += self.dfs(graph, nxt, visited)
        return res


if __name__ == '__main__':

    n = 6
    connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
    ss = Solution()
    res = ss.minReorder(n, connections)

    print(res)
