# Problem 3. Two Sum
# NC Link: https://neetcode.io/problems/two-integer-sum
# LC Link: https://leetcode.com/problems/two-sum/description/

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # make a num dict to hold num and their indices
        num_dict = dict()

        for i in range(len(nums)):
            diff = target - nums[i]

            # We found our solution
            if diff in num_dict:
                return [num_dict[diff], i]
            
            # Else we add and move to the next
            num_dict[nums[i]] = i
            


sol = Solution()
nums = [[2, 7, 11, 15], [3,2,4], [3,3]]
target = [9, 6, 6]
answer = [[0, 1], [1, 2], [0, 1]]

for i in range(len(nums)):
    print(f"Test Case {i + 1}")
    mySolution = sol.twoSum(nums[i], target[i])
    if answer[i] != mySolution:
        print(f"Failure in test case {i + 1}")
    else:
        print("Test Passed!")

"""
Solution:

I struggled with this one. I should have documented my other solutions before landing on the final one.
In short, the problem I had was that I had tried to populate the dictionary first before making the checks for the two sums.
The problem with this was in cases where there are 2 indices for a given solution that belong to the same number. 
I wasn't sure how to make sure I wasn't reusing the same index and it got super convoluted.
Turns out the solution was to basically iterate over the nums array, and consider every value you are looking at as a
potential solution. Then we check, does the diff between the target and the current value equal something that exists in our dictionary.
If so, then we have found the two sum solution. If not, then we add the current value and its index to the dictioary. We are guaranteed
exactly one solution in each case, so we just need to keep checking until we get there.

Time Complexity
    - This gives us an O(n) time complexity because we are iterating over the nums array once. Checking the dictionary is a constant time
        operation as well so this ultimately falls into O(n)

Space Complexity
    - This gives us an O(n) space complexity because at the worst, we would have to create a dictionary that is almost the size of the 
        nums array.
"""