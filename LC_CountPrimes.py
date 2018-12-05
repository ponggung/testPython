class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <3:
            return 0

        digits = [1]*n
        digits[0] = digits[1] = 0

        for i in range(2, int(n**0.5)+1):
            if digits[i] == 1:
                for j in range(i+i, n, i):
                    digits[j] = 0

        return sum(digits)

        #---------------------
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n / 2) + 1):
            if primes[i]:
                primes[i * i:n:i] = [False] * len(primes[i * i:n:i])
        return sum(primes)
        #---------------------


foo = Solution()
n = foo.countPrimes(100)
print(n)
