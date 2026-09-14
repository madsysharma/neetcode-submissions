class Solution:
    def is_within_bounds(self, r: int, c: int, matrix: List[List[int]]) -> bool:
        return 0 <= r < len(matrix) and 0 <= c < len(matrix[0])

    def dfs(self, r: int, c: int, matrix: List[List[int]]) -> int:
        if not self.is_within_bounds(r,c,matrix) or matrix[r][c] == 0:
            return 1
        elif matrix[r][c] == -1:
            return 0
        
        matrix[r][c] = -1
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        tot = 0
        for d in dirs:
            x, y = r + d[0], c + d[1]
            tot += self.dfs(x, y, matrix)
        return tot

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    count += self.dfs(r, c, grid)
        
        return count