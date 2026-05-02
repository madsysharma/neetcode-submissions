class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        # Doing binary search for rows
        for r in range(0,num_rows):
            left = 0
            right = num_cols - 1
            while left <= right:
                mid = left + ((right - left)//2)
                if target < matrix[r][mid]:
                    right = mid - 1
                elif target > matrix[r][mid]:
                    left = mid + 1
                else:
                    return True
        return False


        