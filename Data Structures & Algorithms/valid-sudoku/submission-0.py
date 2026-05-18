from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(list)
        cols = defaultdict(list)
        sqrs = defaultdict(list)

        for r in range(9):           
            for i in board[r]:
                if i.isdigit() and i in rows[r]:
                    print(i)
                    return False
                elif i.isdigit():
                    rows[r].append(i)
        
        print(rows)

        for r in range(9):           
            for c in range(9):
                if board[r][c].isdigit() and board[r][c] in cols[c]:
                    print(c)
                    return False
                elif board[r][c].isdigit():
                    cols[c].append(board[r][c])
        
        print(cols)

        for r in range(9):
            for c in range(9):
                sqrindex = ((r // 3) * 3 + (c // 3))
                if board[r][c].isdigit() and board[r][c] in sqrs[sqrindex]:
                    print(sqrs)
                    return False
                elif board[r][c].isdigit():
                    sqrs[sqrindex].append(board[r][c])
        
        print(sqrs)
        
        return True
        