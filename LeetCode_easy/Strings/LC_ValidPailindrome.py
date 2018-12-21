class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [x.lower() for x in s if x.isalnum()]
        return s == s[::-1]


s = "A man, a plan, a canal: Panama"
foo = Solution()
ans = foo.isPalindrome(s)
print(ans)
