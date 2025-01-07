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
    """
    This code implements a Breadth-First Search (BFS) to find the shortest path 
    in a binary matrix from the top-left corner to the bottom-right corner, 
    where 0 represents a valid path and 1 represents a blocked cell. 
    It marks visited cells in the grid and maintains a dictionary to reconstruct 
    the path to each cell.

    Starting from the top-left, it iteratively explores all valid neighboring cells 
    (up to 8 directions) level by level, updating the path and incrementing the path 
    length until it either reaches the target or exhausts all possible paths.

    If a path to the bottom-right corner exists, it returns the path length and the 
    full path taken; otherwise, it returns -1 and an empty list to indicate no path 
    was found.

    BFS over an N×N grid: In the worst case, the algorithm visits each cell once, leading to 
    O(N ^ 2) queue operations.
    Copying paths for each visit: For each cell we visit, we create a new path by appending the current cell to an existing path, which can take 
    O(N ^ 2) time in the worst case (a path can grow up to 
    O(N ^ 2) length).
    O(N ^ 4)
    O(N ^ 4)
    """
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
                            print(paths) # {(0, 0): [(0, 0)], (1, 1): [(0, 0), (1, 1)]}
            # Increment path length at the conclusion of the level
            path_length += 1

        # If we exit the loop without returning, no path has been found
        return -1, []



ss = Solution()
grid = [[0,0,0],[1,1,0],[1,1,0]]
grid = [[0,1],[1,0]]
res, path = ss.shortestPathBinaryMatrix2(grid)
print(res) #2
print(path)#[(0, 0), (1, 1)]
