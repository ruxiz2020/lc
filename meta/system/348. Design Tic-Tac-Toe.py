class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        # Record count('X') - count('O').
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.antiDiag = 0

    """ Player {player} makes a move at ({row}, {col}).
  
        @param row    The row of the board.
        @param col    The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
    initiate: O(N)
    move: O(1)
    space: O(N)
    """

    def move(self, row: int, col: int, player: int) -> int:
        toAdd = 1 if player == 1 else -1
        target = self.n if player == 1 else -self.n

        if row == col:
            self.diag += toAdd
            if self.diag == target:
                return player

        if row + col == self.n - 1:
            self.antiDiag += toAdd
            if self.antiDiag == target:
                return player

        self.rows[row] += toAdd
        if self.rows[row] == target:
            return player

        self.cols[col] += toAdd
        if self.cols[col] == target:
            return player

        return 0



# Test the TicTacToe class
def test_tic_tac_toe():
    # Initialize a 3x3 TicTacToe board
    ttt = TicTacToe(3)

    # Player 1 moves
    print(ttt.move(0, 0, 1))  # Player 1 moves to (0, 0); Expected: 0 (no winner yet)
    print(ttt.move(0, 1, 2))  # Player 2 moves to (0, 1); Expected: 0 (no winner yet)
    print(ttt.move(1, 1, 1))  # Player 1 moves to (1, 1); Expected: 0 (no winner yet)
    print(ttt.move(0, 2, 2))  # Player 2 moves to (0, 2); Expected: 0 (no winner yet)
    print(ttt.move(2, 2, 1))  # Player 1 moves to (2, 2); Expected: 1 (Player 1 wins)

test_tic_tac_toe()
