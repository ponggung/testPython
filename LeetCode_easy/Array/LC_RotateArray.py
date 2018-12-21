class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 将数组元素依次循环向右平移k个单位
        #  时间复杂度O(n)，空间复杂度O(1)
        n = len(nums)
        idx = 0
        distance = 0
        cur = nums[0]
        for x in range(n):
            idx = (idx + k) % n
            nums[idx], cur = cur, nums[idx]

            distance = (distance + k) % n
            if distance == 0:
                idx = (idx + 1) % n
                cur = nums[idx]
        return nums

    def rotate2(self, nums, k):
        #  时间复杂度O(n)，空间复杂度O(n)
        # 此方法需要构造新的数组，不满足提示描述中的“就地”旋转条件

        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return nums



foo = Solution()
nums = foo.rotate([1, 2, 3, 4, 5, 6, 7], 3)
print(nums)
