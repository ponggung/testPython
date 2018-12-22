'''
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

'''

from itertools import groupby
# import itertools

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int

        數字遍歷 ，如果後面的數字大於前面就減 nums[i]，否則就加上 nums[i]
        因為最後一個數字沒有nums[i+1] 所以要再補零

        """
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        nums = [d[x] for x in s ] +[0]

        digit = 0
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                digit -= nums[i]
            else:
                digit += nums[i]
        return digit




# s = "I"
# s = "III"
s = "IV"
# s = "IX"
# s = "LVIII"
# s = "MCMXCIV"
foo = Solution()
digit = foo.romanToInt(s)
print(digit)