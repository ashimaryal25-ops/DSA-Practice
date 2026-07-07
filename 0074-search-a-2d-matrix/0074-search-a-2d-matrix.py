class Solution(object):
    def searchMatrix(self, matrix, target):
        left = 0
        right = (len(matrix) * len(matrix[0])) - 1
        c = len(matrix[0]) 

        while left <= right:
            mid = (left + right) // 2

            row = mid // c
            col = mid % c

            if matrix[row][col] < target:
   
                left = mid + 1
            elif matrix[row][col] > target:

                right = mid - 1
            else:
                return True
                
        return False  
    
            







        