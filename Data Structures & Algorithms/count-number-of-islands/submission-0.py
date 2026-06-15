class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        visited = set()

        rowlen = len(grid)
        collen = len(grid[0])
        def dfs(row, col):
            if row < 0 or col < 0 or row >= rowlen or col >= collen:
                return
            
            if grid[row][col] == "0" or (row, col) in visited:
                return
            visited.add((row, col))
            for r, c in directions:
                dfs(row + r, col + c)       
        
        count = 0
        for r in range(rowlen):
            for c in range(collen):
                if (r, c) not in visited and grid[r][c] == "1":
                    dfs(r, c)
                    count += 1
        
        return count

        