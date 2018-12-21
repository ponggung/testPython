import collections


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a, b = map(collections.Counter, (nums1, nums2))
        return list((a & b).elements())

        # return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())


nums1 = [1, 2, 3, 3, 3, 1, 2, 3]
nums2 = [2, 2, 2, 3, 4]

foo = Solution()
nums = foo.intersect(nums1, nums2)
print(nums)

# a = collections.Counter(nums1)
# b = collections.Counter(nums2)

# c = list((a & b).elements())
# print(a)
# print(b)
# print(c)
