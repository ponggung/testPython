class Solution:
    def maxSubArray(self, A):
        """
        :type nums: List[int]
        :rtype: int

        """
        if not nums:
            return 0
        current = nums[0]
        m = current
        for i in range(1, len(nums)):
            if current < 0:
                current = 0
            current += nums[i]
            print(current)
            m = max(current, m)
        return m


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums = [-2, 1]
nums = [8, -19, 5, -4, 20]

foo = Solution()
ans = foo.maxSubArray(nums)

print(ans)