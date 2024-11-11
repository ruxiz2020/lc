import collections


class Solution(object):
    def numIslands(self, grid):
        """DFS"""
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        visited = set()
        count = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def findIsland(x, y):
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col and \
                        grid[nx][ny] == '1' and \
                        (nx, ny) not in visited:
                    visited.add((nx, ny))
                    findIsland(nx, ny)

        for x in range(row):
            for y in range(col):
                if grid[x][y] == '1' and (x, y) not in visited:
                    count += 1
                    visited.add((x, y))
                    findIsland(x, y)
        return count


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        m = len(grid)
        n = len(grid[0])

        def bfs(r, c):
            q = collections.deque([(r, c)])
            grid[r][c] = '2'  # Mark '2' as visited.
            while q:
                i, j = q.popleft()
                for dx, dy in dirs:
                    x = i + dx
                    y = j + dy
                    if x < 0 or x == m or y < 0 or y == n:
                        continue
                    if grid[x][y] != '1':
                        continue
                    q.append((x, y))
                    grid[x][y] = '2'  # Mark '2' as visited.

        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bfs(i, j)
                    ans += 1

        return ans


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    ss = Solution()
    res = ss.numIslands(grid)

    print(res)
