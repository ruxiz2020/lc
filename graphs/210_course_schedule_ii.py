import collections
from typing import List

class Solution:
    '''Topological sort'''
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = { c:[] for c in range(numCourses) }
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        visit, cycle = set(), set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit: # if visited skip
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output



if __name__ == '__main__':

    numCourses = 4; prerequisites = [[1,0],[2,0],[3,1],[3,2]]

    ss = Solution()
    res = ss.findOrder(numCourses, prerequisites)

    print(res)
