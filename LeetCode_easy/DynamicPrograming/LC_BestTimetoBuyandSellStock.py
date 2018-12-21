class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) == 0:
            return 0
        profit = 0
        minp = prices[0]
        for p in prices:
            if p < minp:
                minp = p
            elif p - minp > profit:
                profit = p - minp
        return profit





# prices = [7, 1, 5, 3, 6, 4]
# prices = [7, 6, 4, 3, 1]
prices = [2, 1, 2, 0, 1,0,0,0,0,0,100]
# prices = [2, 1, 2, 0, 1]


foo = Solution()
p = foo.maxProfit(prices)
print(p)
