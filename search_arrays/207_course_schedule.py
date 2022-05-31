import collections

class Solution(object):
    def canFinish(self, N, prerequisites):
        """
        :type N,: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.graph = collections.defaultdict(list)
        for u, v in prerequisites:
            self.graph[u].append(v)
        # 0 = Unknown, 1 = visiting, 2 = visited
        self.visitSet = set()
        for crs in range(N):
            if not self.dfs(crs):
                return False
        return True

    # Can we add node i to visited successfully?
    def dfs(self, crs):

        if crs in self.visitSet:
            return False
        if self.graph[crs] == []:
            return True
        self.visitSet.add(crs)

        for pre in self.graph[crs]:
            if not self.dfs(pre):
                return False
        self.visitSet.remove(crs)
        self.graph[crs] = []
        return True



if __name__ == '__main__':

    numCourses = 5; prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]

    ss = Solution()
    res = ss.canFinish(numCourses, prerequisites)

    print(res)
