class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = len(matrix[0])
        rows = len(matrix)
        low = 0
        high = cols*rows-1
        while low<=high:
            mid = (low+high)//2
            row = mid//cols
            col = mid%cols
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                high = cols*row+col-1 #mid-1
            else:
                low = cols*row+col+1 #mid+1
        return False