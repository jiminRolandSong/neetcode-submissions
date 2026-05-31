from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowdict = defaultdict(list)
        coldict = defaultdict(list)
        boxdict = defaultdict(list)

        rowlen = 9
        collen = 9

        for r in range(rowlen):
            for c in board[r]:
                if c.isdigit() and c in rowdict[r]:
                    return False
                elif c.isdigit():
                    rowdict[r].append(c)
        
        for r in range(rowlen):
            for c in range(collen):
                current = board[r][c]
                if current.isdigit() and current in coldict[c]:
                    return False
                elif current.isdigit():
                    coldict[c].append(current)
        
        for r in range(rowlen):
            for c in range(collen):
                boxnum = (r // 3) * 3 + (c // 3)
                current = board[r][c]
                if current.isdigit() and current in boxdict[boxnum]:
                    return False
                elif current.isdigit():
                    boxdict[boxnum].append(current)
        
        return True
        
        


        