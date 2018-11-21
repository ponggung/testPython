'''
解題方法
看了下，這個規模是1000，那麼用O(n^3)的暴力解法肯定就TLE了。那麼只能用更高效的算法。

這個方法是這樣的，我們先對這個數組進行排序，排序之後我們來指出這個三角形中最長的邊，那麼剩下兩條邊的要求是：兩邊之和大於最長邊。

所以，我們只需要對最長邊進行變遍歷，對兩個短邊再遍歷即可。短邊的遍歷方法是：一個從0開始的短邊l，一個從比最長邊的短的一個邊r開始向中間遍歷。如果能夠成三角形，那麼說明比l長的短邊和r結合也都能組成三角形。如果不能組成三角形，那麼說明l太小了，需要向中間移動。

排序算法時間複雜度是O(nlogn)，for循環時間複雜度為O(n)，while循環雖然有兩個變量，但是這兩個變量是同時向中間移動的關係，所以時間複雜度不會超過O(n)，總體的時間複雜度是O(n)。空間複雜度是O(1)。

注意，sorted()函數不是原地排序，如果原地排序需要使用nums.sort()。這就是我第一次提交失敗的地方。
--------------------- 
作者：负雪明烛 
来源：CSDN 
原文：https://blog.csdn.net/fuxuemingzhu/article/details/82630898 
版权声明：本文为博主原创文章，转载请附上博文链接！
'''

class Solution:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = 0
        for i in range(len(nums) - 1, 1, -1):
            l, r = 0, i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    count += r - l
                    r -= 1
                else:
                    l += 1
        return count



solution = Solution()
nums = [2, 2, 3, 4, 5, 5, 6, 7]
count = solution.triangleNumber(nums)
print(count)

# for i in range(len(nums)-1 , 0, -1):
#     print(nums[i])