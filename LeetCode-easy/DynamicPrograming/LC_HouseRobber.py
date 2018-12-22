'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
'''


from itertools import product

class Solution:
    '''
    思路一
    這個問題可以這麼想，假設只有一家，那麼你只能偷這家；假設有兩家，那麼你要判斷兩家哪個錢多，偷哪個；依次類推，假設有n家，那麼你要判斷“偷第n家不偷第n-1家且前n-2家盡量多的偷”和“不偷第n家且前n-1家盡量多的偷”，哪個得到的錢多偷哪個。
    你可以遞歸求解，然而復雜度太高無法AC。所以應該記錄已經計算過的結果，於是這變成一個動態規劃問題。
    --------------------- 
    作者：coder_orz 
    来源：CSDN 
    原文：https://blog.csdn.net/coder_orz/article/details/51555813 
    版权声明：本文为博主原创文章，转载请附上博文链接！
    '''
    def rob1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) < 2:
            return max(nums[0], nums[-1])
        money = [0]*len(nums)
        money[0], money[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            money[i] = max(nums[i] + money[i-2], money[i-1])
            print(i,money)
        return money[len(nums)-1]
    '''
    思路二
    當然你會發現，上面的代碼使用的空間是冗餘的，因為每次循環只會用到前兩個數據。所以代碼可以降低空間複雜度到O(1)。
    '''
    def rob(self, nums):
        now = last = 0
        for i in nums:
            print(i, ":",last, now)
            last, now = now, max(i + last, now)
        return now




foo = Solution()
# nums = [1, 2, 3, 1]
nums = [2, 7, 9, 3, 1]
money = foo.rob1(nums)
print(money)