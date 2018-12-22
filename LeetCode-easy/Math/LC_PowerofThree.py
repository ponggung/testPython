'''
Given an integer, write a function to determine if it is a power of three.
'''


class Solution:
    # Method 1
    def isPowerOfThree1(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n % 3 == 0:
            n /= 3
        return n == 1

    # Method 2
    def isPowerOfThree2(self, n):
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 3 == 0:
            return self.isPowerOfThree(n/3)
        else:
            return False
    # Method 3

    def isPowerOfThree(self, n):
        '''
        可否被 3**19 整除
        '''
        return n > 0 and 3**19 % n == 0


for n in range(1000):
    foo = Solution()
    ans = foo.isPowerOfThree1(n)
    print(n, ans)
