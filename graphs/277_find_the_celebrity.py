def knows(a, b):
    if graph[a][b] == 1:
        return True
    else:
        return False


class Solution:
    def findCelebrity(self, n):
        self.n = n
        for i in range(n):
            if self.is_celebrity(i):
                return i
        return -1

    def is_celebrity(self, i):
        for j in range(self.n):
            if i == j: continue # Don't ask if they know themselves.
            if knows(i, j) or not knows(j, i):
                return False
        return True


if __name__ == '__main__':

    graph = [[1,1,0],[0,1,0],[1,1,1]]
    ss = Solution()
    res = ss.findCelebrity(3)

    print(res)
