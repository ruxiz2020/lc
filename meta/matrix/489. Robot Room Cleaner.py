# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """


class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        # dfs(i, j, d) will perform a Depth-First Search starting from the cell (i, j)
        # facing direction d, using the robot interface to move, turn, and clean.
        def dfs(i, j, d):
            # 1) Mark the current cell as visited.
            vis.add((i, j))

            # 2) Clean the current cell using the robot's clean() method.
            robot.clean()

            # 3) Attempt to move/clean in all 4 directions (relative to current direction).
            #    We do this by turning 0°, 90°, 180°, and 270° from the current heading.
            for k in range(4):
                # nd: new direction after turning k * 90° from the current direction d
                nd = (d + k) % 4

                # Compute the next cell's coordinates (x, y) based on the direction offsets.
                # dirs[nd] is the row offset (dx), dirs[nd+1] is the column offset (dy).
                x, y = i + dirs[nd], j + dirs[nd + 1]

                # 4) Check if the next cell (x, y) hasn't been visited and is not blocked.
                #    robot.move() attempts to move forward; returns True if movement succeeded.
                if (x, y) not in vis and robot.move():
                    # If we can move, recursively explore (x, y) in direction nd
                    dfs(x, y, nd)

                    # 5) Once we've finished exploring (x, y), we need to come back (backtrack)
                    #    to (i, j) facing the original direction d.
                    #    - turnRight() * 2 effectively turns the robot 180 degrees
                    #    - move() makes the robot go back to the original cell
                    #    - turnRight() * 2 again reorients the robot back to the original heading
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()

                # 6) Turn the robot 90° to the right to check the next direction.
                robot.turnRight()

        # dirs defines offsets for moving UP, RIGHT, DOWN, LEFT in a cycle:
        #   -1 for row means move up, +1 for row means move down, etc.
        # By including 5 elements, we can pair them as (dirs[0], dirs[1]) = up,
        # (dirs[1], dirs[2]) = right, and so on in a cyclical manner.
        dirs = (-1, 0, 1, 0, -1)

        # vis keeps track of visited (i, j) cells to avoid re-cleaning or infinite loops.
        vis = set()

        # Start DFS from the initial position (0, 0) with direction 0 (which corresponds
        # to 'up' in our dirs array).
        dfs(0, 0, 0)




class MockRobot:
    def __init__(self, room, start_row, start_col):
        """
        :param room: 2D grid representing the room where 1 is open and 0 is blocked.
        :param start_row: Initial row of the robot.
        :param start_col: Initial column of the robot.
        """
        self.room = room
        self.position = (start_row, start_col)
        self.direction = 0  # 0: up, 1: right, 2: down, 3: left
        self.cleaned = set()

    def move(self):
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left
        next_row = self.position[0] + directions[self.direction][0]
        next_col = self.position[1] + directions[self.direction][1]
        if 0 <= next_row < len(self.room) and 0 <= next_col < len(self.room[0]) and self.room[next_row][next_col] == 1:
            self.position = (next_row, next_col)
            return True
        return False

    def turnLeft(self):
        self.direction = (self.direction - 1) % 4

    def turnRight(self):
        self.direction = (self.direction + 1) % 4

    def clean(self):
        self.cleaned.add(self.position)


# Test Environment
room = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 1]
]

# Starting position (1, 3)
robot = MockRobot(room, 1, 3)

# Test the Solution
solution = Solution()
solution.cleanRoom(robot)

# Verify cleaned cells
print("Cleaned cells:", robot.cleaned)

# Expected Output:
# Cleaned cells should include all reachable cells in the room:
# {(1, 3), (0, 3), (0, 2), (0, 1), (0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (1, 1)}
