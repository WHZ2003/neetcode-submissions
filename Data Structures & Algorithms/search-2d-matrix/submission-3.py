class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m, n = len(matrix), len(matrix[0])

        print(m,n)

        length = m * n 

        mid = (length - 1) // 2
        left = 0
        right = length - 1

        itera = 0 
        while (left <= right and itera < 20):
            # print(left, mid, right)
            row = mid // n
            col = mid - (n * row)
            print(row,col)
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                right = mid - 1
                mid = (right+left)//2
            else:
                left = mid + 1
                mid = (right+left)//2
            
            
            itera += 1
        return False
        