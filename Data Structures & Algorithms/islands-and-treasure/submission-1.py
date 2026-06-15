from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rowlen = len(grid)
        collen = len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        q = deque()
        
        for r in range(rowlen):
            for c in range(collen):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))
        
        def addcell(row, col):
           
            if row < 0 or col < 0 or row == rowlen or col == collen:
                return
            
            if (row, col) in visited or grid[row][col] == -1:
                return
            
            visited.add((row, col))
            q.append([row, col])
        
        distance = 0
        while q:
            print(q)
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
                addcell(r + 1, c)
                addcell(r - 1, c)
                addcell(r, c + 1)
                addcell(r, c - 1)
            distance += 1

        
        