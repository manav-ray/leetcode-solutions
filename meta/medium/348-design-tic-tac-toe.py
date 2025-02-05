"""

Instead of thinking about this as a game simulation, think about the math behind it.
Assign 1 to player1 and -1 to player2:
    - On an NxN grid, we keep track of the sum for each row, col, and diagonal
    - If the sum of any of these == N, player1 wins (-N for player2 to win)
Rows and col are easy (use an array).
For left diagonal, row == col and right diagonal, row + col == N - 1

TC - O(1)
SC - O(n)

"""


class TicTacToe:

    def __init__(self, n: int):
        self.dim = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti = 0

    def move(self, row: int, col: int, player: int) -> int:
        playerVal = 1 if player == 1 else -1
        winningScore = playerVal * self.dim

        self.rows[row] += playerVal
        self.cols[col] += playerVal

        if row == col:
            self.diag += playerVal
        
        if row + col == self.dim - 1:
            self.anti += playerVal

        if (
            self.rows[row] == winningScore
            or self.cols[col] == winningScore
            or self.diag == winningScore
            or self.anti == winningScore
        ):
            return player

        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
