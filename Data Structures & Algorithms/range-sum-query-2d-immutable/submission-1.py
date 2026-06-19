from collections import defaultdict
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rowlen = len(matrix)
        collen = len(matrix[0])

        self.summat = defaultdict(list)

        for r in range(rowlen + 1):
            for c in range(collen + 1):
                self.summat[r].append(0)
        
        for r in range(rowlen):
            prefix = 0
            for c in range(collen):
                prefix += matrix[r][c]
                above = self.summat[r][c + 1]
                self.summat[r+1][c + 1] = (prefix + above)
        


        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        onerow = row1 + 1
        onecol = col1 + 1
        tworow = row2 + 1
        twocol = col2 + 1

        totalsum = self.summat[tworow][twocol]
        upper = self.summat[onerow-1][twocol]
        left = self.summat[tworow][onecol - 1] - self.summat[onerow - 1][onecol - 1]

        return totalsum - upper - left


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)