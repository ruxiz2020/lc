class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0] * n for _ in range(n)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curx = cury = curd = 0
        for i in range(1, n * n + 1):
            res[curx][cury] = i
            newx, newy = curx + directions[curd][0], cury + directions[curd][1]
            if newx < 0 or newx >= n or newy < 0 or newy >= n or res[newx][newy]:
                curd = (curd + 1) % 4
            curx += directions[curd][0]
            cury += directions[curd][1]
        return res
