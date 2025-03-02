# Problem 1. Contains Duplicate
# LC Link: https://leetcode.com/problems/contains-duplicate/description/
# NC Link: https://neetcode.io/problems/duplicate-integer

"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))


# Testing
sol = Solution()
nums = [[1, 2, 3, 1], [1, 2, 3, 4], [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]]

for num in nums:
    print(sol.containsDuplicate(num))

"""
Solution:
    - a set will take a list and remove the duplicates
    - if there are no duplicates, then the original list should be the same length as the set list
    - if not, then there is a duplicate
"""