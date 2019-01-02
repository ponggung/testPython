'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different
'''


class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = bin(x).replace("0b","0")
        y = bin(y).replace("0b", "0")
        n = len(x)-len(y)
        if n <  0:
            x = "0"*abs(n) + x
        elif n > 0:
            y = "0"*abs(n) + y
        print(x,y)
        distance =0
        for i in range(len(x)):
            distance += abs(int(x[i]) - int(y[i]))
        return distance


x,y =1,4
foo = Solution()
distance = foo.hammingDistance(x, y)
print(distance)
