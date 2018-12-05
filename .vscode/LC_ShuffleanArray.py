import random


class Solution:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        return sorted(self.nums, key=lambda x: random.random())

nums = [1,2,3,4,5,6,7,8,9]
foo = Solution(nums)

r = foo.reset()
s = foo.shuffle()

print(r)
print(s)