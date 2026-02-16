# Given an integer array nums, return true if any value appears more than once
# in the array, and otherwise return false.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

class Solution:
    def contains_duplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) < len(nums)

# Time Complexity -> O(n)
# Space Complexity -> O(n)