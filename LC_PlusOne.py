class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        integer = 0
        digits = digits[::-1]
        for i in range(len(digits)-1, -1, -1):
            integer += digits[i] * 10 ** i
        print(integer)
        integer += 1
        digits= []
        for i in str(integer):
            digits.append(int(i))
        return digits


foo = Solution()
digits = foo.plusOne([1,2,3,4])
print(digits)
digits = foo.plusOne([9,9,9])
print(digits)

nn = [9, 9, 9]
nn.insert(0, 1)
print(nn)
