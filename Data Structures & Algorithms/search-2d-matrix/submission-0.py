class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        lowercol = 0
        uppercol = len(matrix[0]) - 1

        lowerrow = 0
        upperrow = len(matrix) - 1

        while upperrow >= lowerrow:
            mid = (upperrow + lowerrow) // 2
            print(mid)
            lastcol = len(matrix[0]) - 1

            if matrix[mid][lastcol] == target or matrix[mid][0] == target:
                return True

            if target > matrix[mid][0] and target < matrix[mid][lastcol]:
                print("middle", mid)
                while lowercol < uppercol:
                    colmid = (lowercol + (uppercol - lowercol) // 2)

                    if matrix[mid][colmid] == target:
                        return True
                    elif matrix[mid][colmid] < target:
                        lowercol = colmid + 1
                    else:
                        uppercol = colmid - 1
                
                return False

            elif target < matrix[mid][0]:
                upperrow = mid - 1

            else:
                lowerrow = mid + 1


            
        return False
        