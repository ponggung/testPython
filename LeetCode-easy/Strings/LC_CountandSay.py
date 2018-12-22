import itertools


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = "1"
        for i in range(n-1):
            res = ''.join([str(len(list(group))) + digit for digit, group in itertools.groupby(res)])
        return res


foo =Solution()
n = 5
res = foo.countAndSay(n)
print(res)


for digit, group in itertools.groupby('aabbbbaccc'):
    print(digit, ':', len(list(group)))
