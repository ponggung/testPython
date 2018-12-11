class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        '''1'''
        #         lz = nums.count(0)
        #         for i in range(lz):
        #             nums.append(0)

        #         i = 0
        #         while lz:
        #             if nums[i] == 0:
        #                 del nums[i]
        #                 lz -= 1
        #             else:
        #                 i += 1
        '''2'''
        # i = 0
        # for num in nums:
        #     if num != 0:
        #         nums[i] = num
        #         i += 1
        # for j in range(i, len(nums)):
        #     nums[j] = 0

        '''3'''
        nums.sort(key=lambda x: 1 if x == 0 else 0)
        print(nums)


nums = [0, 1, 0, 3, 12]
foo = Solution()
foo.moveZeroes(nums)
