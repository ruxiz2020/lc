class Direction:
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'


class Mouse:

    def move(self, direction):
        """
        Moves to one of the directions (left, right, up, down) and
        returns False if you can't move, and True if you can.
        """
        # Move implementation is provided externally
        return True

    def has_cheese(self):
        """
        Returns True if there is a cheese in the current cell.
        """
        # Cheese detection implementation provided externally
        return False

    def get_cheese(self):
        """
        Should return True and leave the mouse at the cheese location,
        or False if we can't find cheese, returning the mouse to its starting point.
        """
        return self._dfs()

    def _dfs(self):
        # Check if we have cheese at the current cell
        if self.has_cheese():
            return True

        # Try each direction
        for direction in [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]:
            # Attempt to move in the direction
            if self.move(direction):
                # If moving in this direction finds cheese, return True
                if self._dfs():
                    return True
                # Backtrack if cheese was not found in this path
                self.move(self._opposite(direction))

        return False  # Return False if no cheese found in any direction

    def _opposite(self, direction):
        """
        Helper function to get the opposite direction for backtracking.
        """
        opposites = {
            Direction.UP: Direction.DOWN,
            Direction.DOWN: Direction.UP,
            Direction.LEFT: Direction.RIGHT,
            Direction.RIGHT: Direction.LEFT
        }
        return opposites[direction]





class MockMouse(Mouse):
    def __init__(self, grid, start_row, start_col):
        """
        :param grid: 2D grid where 1 represents cheese, 0 represents free space, -1 represents a wall.
        :param start_row: Starting row position of the mouse.
        :param start_col: Starting column position of the mouse.
        """
        self.grid = grid
        self.position = (start_row, start_col)
        self.visited = set()

    def move(self, direction):
        directions = {
            Direction.UP: (-1, 0),
            Direction.DOWN: (1, 0),
            Direction.LEFT: (0, -1),
            Direction.RIGHT: (0, 1),
        }
        next_row = self.position[0] + directions[direction][0]
        next_col = self.position[1] + directions[direction][1]

        if 0 <= next_row < len(self.grid) and 0 <= next_col < len(self.grid[0]) and self.grid[next_row][next_col] != -1:
            self.position = (next_row, next_col)
            return True
        return False

    def has_cheese(self):
        row, col = self.position
        return self.grid[row][col] == 1


# Test Environment
grid = [
    [0, 0, 0, 0],
    [0, -1, -1, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0]
]

# Mouse starts at (0, 0)
mock_mouse = MockMouse(grid, 0, 0)

# Test the Solution
result = mock_mouse.get_cheese()
print("Found cheese:", result)  # Expected Output: True
print("Mouse position after finding cheese:", mock_mouse.position)  # Expected: (2, 2)
