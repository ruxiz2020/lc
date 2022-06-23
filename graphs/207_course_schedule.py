import collections
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs
        preMap = { i:[] for i in range(numCourses)}

        # map each course to : prereq list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()
        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c): return False
        return True



if __name__ == '__main__':

    numCourses = 5; prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]

    ss = Solution()
    res = ss.canFinish(numCourses, prerequisites)

    print(res)
