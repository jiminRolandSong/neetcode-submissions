class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rowlen = len(heights)
        collen = len(heights[0])
        pacstart = set()
        atlstart = set()

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for r in range(rowlen):
            pacstart.add((r, 0))
            atlstart.add((r, collen - 1))
        
        for c in range(collen):
            pacstart.add((0, c))
            atlstart.add((rowlen -1, c))
        
        pac_available = set()
        atl_available = set()

        def dfs(row, col, visited, prevHeight):
            if row < 0 or col < 0 or row == rowlen or col == collen:
                return
            
            if (row, col) in visited or heights[row][col] < prevHeight:
                return
            
            visited.add((row, col))

            for rd, cd in directions:
                dfs(row+ rd, col + cd, visited, heights[row][col])
        
        for row, col in pacstart:
            dfs(row, col, pac_available, heights[row][col])
        
        for row, col in atlstart:
            dfs(row, col, atl_available, heights[row][col])
        
        result = []
        for r in range(rowlen):
            for c in range(collen):
                if (r, c) in pac_available and (r, c) in atl_available:
                    result.append((r, c))
        
        return result

            


        