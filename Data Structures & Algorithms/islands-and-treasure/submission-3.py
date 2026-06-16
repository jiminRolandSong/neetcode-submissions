from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rowlen = len(grid)
        collen = len(grid[0])

        visited = set()
        directions = [(1,0), (0, 1), (-1, 0), (0, -1)]
        q = deque()

        for r in range(rowlen):
            for c in range(collen):
                if grid[r][c] == 0:
                    q.append((r, c))

        def bfs(row, col):
            if row < 0 or col < 0 or row == rowlen or col ==collen:
                return False
            
            if (row, col) in visited or grid[row][col] < 0:
                return False
            
            visited.add((row, col))
            for rd, cd in directions:
                q.append((row + rd, col + cd))
            
            return True
        
        distance = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                if (row, col) not in visited and bfs(row, col):
                    grid[row][col] = distance
            
            distance += 1



        