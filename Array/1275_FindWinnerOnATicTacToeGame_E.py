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

# Solution 2: naive solution
class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        n = 3
        grid = [[' '] * n for _ in range(n)]
        
        for idx in range(len(moves)):
            player = 'A' if idx % 2 == 0 else 'B'
            i = moves[idx][0]
            j = moves[idx][1]
            
            grid[i][j] = player
            
            # check column
            cnt = 0
            for c in range(n):
                if grid[i][c] == player:
                    cnt += 1
            if cnt == n:
                return player
            
            # check row
            cnt = 0
            for r in range(n):
                if grid[r][j] == player:
                    cnt += 1
            if cnt == n:
                return player
            
            # check maindiag
            if i == j:
                cnt = 0
                for d in range(n):
                    if grid[d][d] == player:
                        cnt += 1
                if cnt == n:
                    return player
                
            # check antidiag
            if i == (n-1-j):
                cnt = 0
                for d in range(n):
                    if grid[d][n-1-d] == player:
                        cnt += 1
                if cnt == n:
                    return player
        
        # no winner after all moves
        
        if len(moves) == n**2:
            return 'Draw'
        
        return 'Pending'
    
