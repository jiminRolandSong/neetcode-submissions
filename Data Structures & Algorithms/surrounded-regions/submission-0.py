class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rowlen = len(board)
        collen = len(board[0])

        visited = set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]


        def dfs(row, col):
            if row < 0 or col < 0 or row == rowlen or col == collen:
                return
            
            if board[row][col] == 'X' or (row, col) in visited:
                return
            
            visited.add((row, col))
            
            for rd, cd in directions:
                dfs(row + rd, col + cd)
        
        starts = set()

        for r in range(rowlen):
            starts.add((r, 0))
            starts.add((r, collen - 1))
        
        for c in range(collen):
            starts.add((0, c))
            starts.add((rowlen - 1, c))
        
        for row, col in starts:
            if board[row][col] == 'O':
                dfs(row, col)
        
        for r in range(rowlen):
            for c in range(collen):
                if (r, c) not in visited:
                    board[r][c] = 'X' 

        