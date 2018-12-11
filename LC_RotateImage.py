matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]]

matrix =[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]]
class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i+1 , n):
                print(i,j)
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        return matrix

foo = Solution()
matrix = foo.rotate(matrix)
print(matrix)
