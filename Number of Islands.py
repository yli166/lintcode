class Solution:
    """
    @param: grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid):
        # write your code here
        if grid == []:
            return 0
        m = len(grid)
        n = len(grid[0])

        visited = [[False for i in range(n)] for i in range(m)]
        count = 0

        for i in range(m):
            for each in range(n):
                if grid[i][each] == 1 and visited[i][each] == False:
                    count += 1
                    self.change(grid, visited, i, each)

        return count

    def change(self, grid, visited, row, col):
        m = len(grid)
        n = len(grid[0])

        if row < 0 or row >= m or col < 0 or col >= n:
            return False

        if grid[row][col] == 1 and visited[row][col] == False:
            visited[row][col] = True
            if self.change(grid, visited, row - 1, col) or self.change(grid, visited, row + 1, col) or self.change(grid,
                                                                                                                   visited,
                                                                                                                   row,
                                                                                                                   col + 1) or self.change(
                    grid, visited, row, col - 1):
                return True

        return False

