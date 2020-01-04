# https://leetcode.com/problems/game-of-life/

# Solution 1:
'''
curr_ij    num_live_neighbors    next_ij    next_ij,curr_ij
1          < 2                   0          01 = curr_ij
1          2, 3                  1          11 = curr_ij + 2 = curr_ij | 2
1          > 3                   0          01 = curr_ij
0          3                     1          10 = curr_ij + 2 = curr_ij | 2
0          != 3                  0          00 = curr_ij
'''
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def get_num_live_neighbors(i, j):
            num = 0
            for r in range(max(0, i-1), min(m-1, i+1)+1):
                for c in range(max(0, j-1), min(n-1, j+1)+1):
                    if (r, c) != (i, j) and board[r][c]%2 == 1:
                        num += 1
            return num

        if len(board) == 0 or len(board[0]) == 0:
            return

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                num_live_neighbors = get_num_live_neighbors(i, j)
                if (board[i][j]%2 == 1 and num_live_neighbors in [2, 3]) or (board[i][j]%2 == 0 and num_live_neighbors in [3]):
                    board[i][j] |= 2 # board[i][j] += 2

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1

        return

# Solution 2: infinite board
# https://leetcode.com/problems/game-of-life/discuss/73217/Infinite-board-solution
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def gameOfLife_infinite(live_cells):
            ctr = collections.Counter((r, c) for (i, j) in live_cells for r in range(i-1, i+2) for c in range(j-1, j+2) if (r, c) != (i, j))

            return {(i,j) for (i,j) in ctr if ctr[(i,j)] == 3 or (ctr[(i,j)] == 2 and (i,j) in live_cells)}

        if len(board) == 0 or len(board[0]) == 0:
            return

        m, n = len(board), len(board[0])

        lc = {(i,j) for i in range(m) for j in range(n) if board[i][j] == 1}
        lc = gameOfLife_infinite(lc)

        for i in range(m):
            for j in range(n):
                board[i][j] = int((i,j) in lc)

        return
        
