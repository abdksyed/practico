# Given two strings s and t, return true if the two strings are anagrams
# of each other, otherwise return false.

# An anagram is a string that contains the exact same characters
# as another string, but the order of the characters can be different.

# Example 1:
# Input: s = "racecar", t = "carrace"
# Output: true

# Example 2:
# Input: s = "jar", t = "jam"
# Output: false

class Solution:
    def check_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_s = {}
        map_t = {}
        for i,j in zip(s,t):
            map_s[i] = map_s.get(i,0) + 1
            map_t[j] = map_t.get(j,0) + 1
        return map_s == map_t
        
