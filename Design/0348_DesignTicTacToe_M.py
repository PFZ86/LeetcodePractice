# https://www.cnblogs.com/lightwindy/p/9649759.html

# Solution 1: keep row_sums, col_sums, maindiag_sum, antidiag_sum; O(n) time; O(n) space
class TicTacToe(object):
    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.row_sums = [0] * n
        self.col_sums = [0] * n
        self.maindiag_sum = 0
        self.antidiag_sum = 0

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        assert player == 1 or player == 2
        score = 3 - 2 * player # 1 for player 1; -1 for player 2
        self.row_sums[row] += score
        self.col_sums[col] += score
        if row == col:
            self.maindiag_sum += score
        if row == (self.n - 1 - col):
            self.antidiag_sum += score

        if abs(self.row_sums[row]) == self.n \
        or abs(self.col_sums[col]) == self.n \
        or abs(self.maindiag_sum) == self.n \
        or abs(self.antidiag_sum) == self.n:
            return player

        return 0
        
