from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res = []
        paths = [[0]]
        while paths:
            tmp = []
            for path in paths:
                if path[-1] == n - 1:
                    res.append(path)
                    continue
                for node in graph[path[-1]]:
                    tmp.append(path + [node])
            paths = tmp
        return res


if __name__ == '__main__':

    graph = [[1,2],[3],[3],[]]
    ss = Solution()
    res = ss.allPathsSourceTarget(graph)

    print(res)
