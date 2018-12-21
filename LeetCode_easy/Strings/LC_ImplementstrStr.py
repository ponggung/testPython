class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        elif needle not in haystack:
            return -1
        return haystack.index(needle)


h = "hello"
n = "ll"
foo = Solution()
ans = foo.strStr(h,n)
print(ans)