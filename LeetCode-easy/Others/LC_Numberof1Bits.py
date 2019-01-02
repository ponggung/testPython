class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count("1")


n= 11
foo = Solution()
foo.hammingWeight(n)
bit = foo.hammingWeight(n)
print(bit)