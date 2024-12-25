

class Solution(object):
    """
    O(M * N)
    O(p), p: count of 1s
    """
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        x = list()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x.append(i)
        print(x) # [0, 0, 2]

        if len(x) == 0:
            return 0

        size = len(x)
        y = list()
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                if grid[i][j] == 1:
                    y.append(j)

        print(y) # [0, 2, 4]

        if size % 2 == 1:
            X, Y = x[size // 2], y[size // 2]
        else:
            xm = sum(x[size // 2 - 1:size // 2 + 1]) / 2
            ym = sum(y[size // 2 - 1:size // 2 + 1]) / 2
            print(xm, ym)

            X, Y = round(xm), round(ym)
        print(X, Y)

        return sum([abs(X - x_) for x_ in x]) + sum([abs(Y - y_) for y_ in y])


if __name__ == '__main__':

    grid = [[1,0,0,0,1],
            [0,0,0,0,0],
            [0,0,1,0,0]]

    # grid = [[1,1]]
    ss = Solution()
    res = ss.minTotalDistance(grid)

    print(res)
