from typing import List
import collections

class Solution:
    """time: O(n)
    sapce: O(n)"""
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        start at city 0
        recursively check its neighbors
        count outgoing edges
        """

        edges = {(a, b) for a, b in connections}
        neighbors = {city: [] for city in range(n)}
        visit = set()
        changes = 0

        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        def dfs(city):
            nonlocal edges, neighbors, visit, changes

            for neighbors in neighbors[city]:
                if neighbors in visit:
                    continue
                """check if this neighbor can reach city 0"""
                if (neighbors, city) not in edges:
                    changes += 1
                visit.add(neighbors)
                dfs(neighbors)
        visit.add(0)
        dfs(0)
        return changes



if __name__ == '__main__':

    n = 6
    connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
    ss = Solution()
    res = ss.minReorder(n, connections)

    print(res)
