class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        x = int(str(x)[::-1]) if x >= 0 else -int(str(-x)[::-1])
        return x if x < (2**31 - 1) and x >= (-2**31) else 0


num = Solution()
print(num.reverse(123456789))
print(num.reverse(-245))
print(num.reverse(111111111111111))
