from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Check if the starting cell is blocked
        if grid[0][0] != 0:
            return -1

        # Initialize the size of the grid
        n = len(grid)
        # Set starting point as visited by marking it with a 1 (path length from the origin)
        grid[0][0] = 1
        # Initialize a queue with the starting coordinate
        queue = deque([(0, 0)])
        # Initialize path length
        path_length = 1

        # Process nodes until the queue is empty
        while queue:
            # Loop through all nodes at the current level of breadth
            for _ in range(len(queue)):
                i, j = queue.popleft()  # Get next node coordinates

                # Check if we've reached the target cell
                if i == j == n - 1:
                    return path_length

                # Check all 8 adjacent cells
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        # Boundary check and cell is not blocked
                        if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                            # Mark cell as visited and add its coordinates to the queue
                            grid[x][y] = 1
                            queue.append((x, y))
            # Increment path length at the conclusion of the level
            path_length += 1

        # If we exit the loop without returning, no path has been found
        return -1



from typing import List, Tuple, Deque
from collections import deque

class Solution:
    def shortestPathBinaryMatrix2(self, grid: List[List[int]]) -> Tuple[int, List[Tuple[int, int]]]:
        # Check if the starting cell is blocked
        if grid[0][0] != 0:
            return -1, []

        # Initialize the size of the grid
        n = len(grid)
        # Set starting point as visited by marking it with a 1 (path length from the origin)
        grid[0][0] = 1
        # Initialize a queue with the starting coordinate
        queue = deque([(0, 0)])
        # Dictionary to store paths with each cell pointing to its previous cell
        paths = {(0, 0): [(0, 0)]}
        # Initialize path length
        path_length = 1

        # Process nodes until the queue is empty
        while queue:
            # Loop through all nodes at the current level of breadth
            for _ in range(len(queue)):
                i, j = queue.popleft()  # Get next node coordinates

                # Check if we've reached the target cell
                if i == j == n - 1:
                    # Return the path length and the path to the target cell
                    return path_length, paths[(i, j)]

                # Check all 8 adjacent cells
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        # Boundary check and cell is not blocked
                        if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                            # Mark cell as visited
                            grid[x][y] = 1
                            # Add its coordinates to the queue
                            queue.append((x, y))
                            # Record the path to reach this cell
                            paths[(x, y)] = paths[(i, j)] + [(x, y)]
                            print(paths)
            # Increment path length at the conclusion of the level
            path_length += 1

        # If we exit the loop without returning, no path has been found
        return -1, []



ss = Solution()
grid = [[0,0,0],[1,1,0],[1,1,0]]
grid = [[0,1],[1,0]]
res, path = ss.shortestPathBinaryMatrix2(grid)
print(res) #2
print(path)
