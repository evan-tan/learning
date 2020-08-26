"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

# Brute force, O(n^2)
def twoSum(self, nums: List[int], target: int) -> List[int]:
    indices = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if (nums[i]+nums[j]) == target:
                indices = [i,j]
    return indices
