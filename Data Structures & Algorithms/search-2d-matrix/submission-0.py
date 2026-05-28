class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        arr = None
        while l <= r:
            arr = (l + r) // 2
            if target < matrix[arr][0]:
                r = arr - 1
            elif target > matrix[arr][-1]:
                l = arr + 1
            else:
                break
        if arr == None: return False
        
        l = 0
        r = len(matrix[arr]) - 1
        while l <= r:
            mid = (l + r) // 2
            if target < matrix[arr][mid]:
                r = mid - 1
            elif target > matrix[arr][mid]:
                l = mid + 1
            else:
                return True
        
        return False