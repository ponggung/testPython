'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
numRows = 5


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        Output = [[1]]
        if numRows==0:
            return []
        for l in range(numRows -1):
            row = Output[l][:] # call by value, not by reference
            row.append(0)
            row.insert(0, 0)
            new_row = []

            for i in range(len(row) -1 ):
                new_row.append(row[i] + row[i+1])
            Output.append(new_row)


        return Output
        
    def generate2(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(0, numRows):
            res.append([1]*(i+1))
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res

foo =Solution()
Output = foo.generate(5)
print(Output)
