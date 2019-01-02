'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''


class Solution(object):
    # method 1
    def missingNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        i = 0
        while i < len(nums):
            if nums[i] != i:
                return i
            else:
                i += 1
        return i
    # method 2
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp_sum = len(nums)*(len(nums)+1)/2
        t_sum = sum(nums)
        return temp_sum - t_sum




nums = [3, 0, 1]
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
# nums = [0]
# nums = [0,1]
foo = Solution()
i = foo.missingNumber(nums)
print(i)
