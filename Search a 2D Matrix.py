class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 
        for ele in matrix:
            for j in ele:
                
                if j == target:
                    print(j)
                    return True
                