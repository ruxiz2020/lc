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
