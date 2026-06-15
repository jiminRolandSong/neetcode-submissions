class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rowlen = len(grid)
        collen = len(grid[0])

        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
        visited = set()

        def dfs(row, col):
            if row < 0 or col < 0 or row >= rowlen or col >= collen:
                return 0
            
            if (row, col) in visited or grid[row][col] == 0:
                return 0
            
            visited.add((row, col))
            area = 1

            for r, c in directions:
                area += dfs(row + r, col + c)
            
            return area
        
        max_area = 0

        for r in range(rowlen):
            for c in range(collen):
                if (r, c) not in visited and grid[r][c] == 1:
                    new_area = dfs(r, c)
                    max_area = max(new_area, max_area)
        
        return max_area
