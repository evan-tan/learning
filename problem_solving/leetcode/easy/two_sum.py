"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.dictionary(nums, target)
        # return self.brute_force(nums,target)

    def dictionary(self, nums, target):
        """O(n)"""
        complement_nums = dict()
        for index, num in enumerate(nums):
            complement = target - num
            if num in complement_nums:
                return index, complement_nums[num]
            else:
                complement_nums[complement] = indexc

    def brute_force(self, nums, target):
        """ O(n^2)"""
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return i,j
