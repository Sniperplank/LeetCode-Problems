# Probelm Description
"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

# Output Examples
"""
Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false
"""

# Problem Solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
