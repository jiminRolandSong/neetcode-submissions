from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rowlen = len(grid)
        collen = len(grid[0])

        q = deque()
        visited = set()

        self.fresh_count = 0

        for r in range(rowlen):
            for c in range(collen):
                if grid[r][c] == 1:
                    self.fresh_count += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
        
        print(self.fresh_count)
        def add(row, col):
            if row < 0 or col < 0 or row >= rowlen or col >= collen:
                return
            
            if (row, col) in visited:
                return
            
            if grid[row][col] == 1:
                grid[row][col] == 2
                self.fresh_count -= 1
                q.append((row, col))
            
            visited.add((row, col))
            return
            
        
        minutes = 0
        while self.fresh_count > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()
                add(r + 1, c)
                add(r - 1, c)
                add(r, c + 1)
                add(r, c - 1)
            minutes += 1
        print(self.fresh_count)
        return minutes if self.fresh_count == 0 else -1
        




        