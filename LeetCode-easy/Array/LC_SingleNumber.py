'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        print(nums)
        for i in range(0, len(nums)-1 , 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]


foo = Solution()
nums = [17, 12, 5, -6, 12, 4, 17, -5, 2, -3,
        2, 4, 5, 16, -3, -4, 15, 15, -4, -5, -6]
n = foo.singleNumber(nums)
print(n)
