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
        visited = set()
        count = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def findIsland(x, y):
            q = collections.deque()
            visited.add((x, y))
            q.append((x, y))

            while q:
                x, y = q.popleft()
                # x, y = q.pop() # DFS
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < row and 0 <= ny < col and \
                        grid[nx][ny] == '1' and \
                        (nx, ny) not in visited:
                        q.append((nx, ny))
                        visited.add((nx, ny))

        for x in range(row):
            for y in range(col):
                if grid[x][y] == '1' and (x, y) not in visited:
                    count += 1
                    visited.add((x, y))
                    findIsland(x, y)
        return count


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
