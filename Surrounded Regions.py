class Solution:
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """

    def surroundedRegions(self, board):
        # write your code here
        if board == []:
            return 0
        bottom = len(board) - 1
        right = len(board[0]) - 1
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(len(board[0])):
            if visited[0][i] == False and board[0][i] == 'O':
                self.change(board, visited, 0, i)
            if visited[bottom][i] == False and board[bottom][i] == 'O':
                self.change(board, visited, bottom, i)
        for i in range(len(board)):
            if visited[i][0] == False and board[i][0] == 'O':
                self.change(board, visited, i, 0)
            if visited[i][right] == False and board[i][right] == 'O':
                self.change(board, visited, i, right)
        for i in range(len(board[0])):
            for j in range(len(board)):
                if board[j][i] == 'O' and visited[j][i] == False:
                    board[j][i] = 'X'

        return board

    def change(self, board, visited, row, col):
        m = len(board)
        n = len(board[0])

        if row < 0 or row >= m or col < 0 or col >= n:
            return False

        if board[row][col] == 'O' and visited[row][col] == False:
            visited[row][col] = True
            if self.change(board, visited, row - 1, col) or self.change(board, visited, row + 1, col) or self.change(
                    board, visited, row, col + 1) or self.change(board, visited, row, col - 1):
                return True

        return False