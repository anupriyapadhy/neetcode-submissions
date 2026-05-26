class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,row,bottom,cols=0,0,len(matrix)-1,len(matrix[0])-1
        while top<=bottom:
            if matrix[top][cols]==target:
                return True
            elif matrix[top][cols]>target and cols>=0:
                cols-=1
            else:
                top+=1
        return False

        