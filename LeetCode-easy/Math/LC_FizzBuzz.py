class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # s = []
        # for num in range(1,n+1):
        #     string = ""
        #     if num % 3 == 0:
        #         string = string + "Fizz"
        #     if num % 5 == 0:
        #         string = string + "Buzz"
        #     if num % 5 != 0 and num % 3 != 0:
        #         string = string + str(num)
        #     s.append(string)
        # return s
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]


foo = Solution()
s = foo.fizzBuzz(100)
print(s)
