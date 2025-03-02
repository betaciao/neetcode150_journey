# Problem 1. Contains Duplicate
# NC Link: https://neetcode.io/problems/is-anagram
# LC Link: https://leetcode.com/problems/valid-anagram/description/

"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

You should aim for a solution with O(n + m) time and O(1) space, where n is the length of the 
string s and m is the length of the string t.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If not same length, can't be an anagram
        if (len(s) != len(t)):
            return False
        
        s_dict = self.makeDict(s)
        t_dict = self.makeDict(t)

        if s_dict == t_dict:
            return True
        else:
            return False
        
    def isAnagram2(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        
    def makeDict(self, s: str) -> dict:
        "makes a frequency dictionary of letters in a string"
        str_dict = dict()
        for letter in s:
            if letter in str_dict.keys():
                str_dict[letter] += 1
            else:
                str_dict[letter] = 1

        return str_dict


# Testing
sol = Solution()
s = ["anagram", "rat"]
t = ["nagaram", "car"]
ans_key = [True, False]

for i in range(len(s)):
    print(f"Test Case #{i+1}")
    myAnswer = sol.isAnagram2(s[i], t[i])
    print(f"Correct Answer: {ans_key[i]}")
    print(f"My Answer: {myAnswer}\n")

"""
Solution 1:
    - my initial thought was that I can make a frequency dictionary of each string where key is paired with its occurence amount
    - also realized, to be an anagram that the length of the strings should be the same so that is a check to start with
    - once frequency dicts have been made, then we can just compare them and make sure they are equal

    Time Complexity: O(s + t) since we are iterating over each of the strings to make the frequency dicts
    Space Complexity: O(s + t) since at worst each string consists of unique characters.

Solution 2:
    - after listening to neetcode, it seems that we could use sorting function since that is sometimes considered not using space
    - this makes things much easier, just compare the sorted version of the strings to one another
    
    Time Complexity: O(s + t) since we are sorting each of the strings
    Space Complexity: O(1) as I think the assumption is that sorted does not take up space
"""