# https://leetcode.com/problems/valid-tic-tac-toe-state/

# Solution 1
class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        n = len(board)
        num_x = 0
        num_o = 0
        row_sums = [0] * n
        col_sums = [0] * n
        maindiag_sum = 0
        antidiag_sum = 0
        for row in range(n):
            for col in range(n):
                if board[row][col] == 'X':
                    num_x += 1
                    row_sums[row] += 1
                    col_sums[col] += 1
                    if row == col:
                        maindiag_sum += 1
                    if (row + col) == (n - 1):
                        antidiag_sum += 1
                if board[row][col] == 'O':
                    num_o += 1
                    row_sums[row] -= 1
                    col_sums[col] -= 1
                    if row == col:
                        maindiag_sum -= 1
                    if (row + col) == (n - 1):
                        antidiag_sum -= 1

        # num_x should be num_o or num_o + 1
        if num_x != num_o and num_x != (num_o + 1):
            return False

        # check who wins
        x_win = False
        o_win = False
        # check rows
        for row in range(n):
            if row_sums[row] == n:
                x_win = True
            if row_sums[row] == -n:
                o_win = True
        # check columns
        for col in range(n):
            if col_sums[col] == n:
                x_win = True
            if col_sums[col] == -n:
                o_win = True
        # check main diagonal
        if maindiag_sum == n:
            x_win = True
        if maindiag_sum == -n:
            o_win = True
        # check anti diagonal
        if antidiag_sum == n:
            x_win = True
        if antidiag_sum == -n:
            o_win = True

        if o_win:
            # x and o can't win at the same time
            if x_win:
                return False
            # if o wins, x and o should have played same steps
            return num_x == num_o
        # if x wins, x should have played 1 more step than o
        if x_win and num_x != (num_o+1):
            return False

        return True
        
