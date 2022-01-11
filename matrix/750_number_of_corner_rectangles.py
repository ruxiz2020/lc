class Solution(object):
    def countCornerRectangles(self, grid):
        res = 0
        counts = [[0] * len(grid[rows]) for rows in range(len(grid))]
        for row in range(0, len(grid)):
            for j in range(1, len(grid[0])):
                if grid[row][j] == 1:
                    for i in range(0, j):
                        if grid[row][i] == 1:
                            res += counts[i][j]
                            counts[i][j] += 1
        return int(res)


if __name__ == '__main__':

    grid = [[1,1,1],[1,1,1],[1,1,1]]

    ss = Solution()
    res = ss.countCornerRectangles(grid)

    print(res)
