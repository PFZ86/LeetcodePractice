# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

# Solution 1:
# (1) 1 for player A and -1 for player B.
# (2) Keep track of row_sums, col_sums, maindiag_sum and antidiag_sum.
# (3) Only the player making the current move can win a game.
class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        n = 3
        row_sums = [0 for _ in range(n)]
        col_sums = [0 for _ in range(n)]
        maindiag_sum = 0
        antidiag_sum = 0

        for idx, (row, col) in enumerate(moves):
            player = "A" if idx % 2 == 0 else "B"
            score = 1 if idx % 2 == 0 else -1

            row_sums[row] += score
            if abs(row_sums[row]) == n:
                return player

            col_sums[col] += score
            if abs(col_sums[col]) == n:
                return player

            if row == col:
                maindiag_sum += score
                if abs(maindiag_sum) == n:
                    return player

            if (row + col) == (n - 1):
                antidiag_sum += score
                if abs(antidiag_sum) == n:
                    return player

        return "Draw" if len(moves) == (n**2) else "Pending"
        
