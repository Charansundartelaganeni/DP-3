#TC: O(n)
#SC: O(1)

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix) #Initializing n as the length of the martix
        for i in range(n-2, -1, -1):   #we are traversing from the reverse
            for j in range(n):  
                if j==0:    #If the the element is in first column the matrix[i][j] is equal to minimum between next row and current column element and next row and next column element
                    matrix[i][j] += min(matrix[i+1][j], matrix[i+1][j+1])
                elif j==n-1:     #If the the element is in last column the matrix[i][j] is equal to minimum between next row and current column element and next row and previous column element
                    matrix[i][j] += min(matrix[i+1][j], matrix[i+1][j-1])
                else:   #else matrix[i][j] is equal to minimum between next row and column before that and next row and next column element
                    matrix[i][j] += min(matrix[i+1][j-1], matrix[i+1][j], matrix[i+1][j+1])
                    
        return min(matrix[0])   #minimum in the first row has the best path