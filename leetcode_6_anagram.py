# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # same length, same  character and its count
        if len(s) == len(t):
            set_s = set(s)
            for i in set_s:
                if s.count(i) != t.count(i):
                    return False
            return True
        else:
            return False

t = Solution()
t.isAnagram('naga','ana')