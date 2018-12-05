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
