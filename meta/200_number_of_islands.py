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

class Solution(object):
    def numIslands(self, grid):
        """BFS"""
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        visit = set()
        island = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                #row, col = q.pop() # dfs
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if 0 <= r < row and 0 <= c < col and \
                        grid[r][c] == '1' and \
                        (r, c) not in visit:
                        q.append((r, c))
                        visit.add((r, c))

        for x in range(row):
            for y in range(col):
                if grid[x][y] == '1' and (x, y) not in visit:
                    bfs(x, y)
                    island += 1
        return island


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
