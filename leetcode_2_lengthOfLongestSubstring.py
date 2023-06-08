# Given a string s, find the length of the longest
# substring
# without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

class Solution(object):
  def lengthOfLongestSubstring(self,s):
    l = list(s)
    maxlen = 0
    news = ''
    for index,i in enumerate(l):
      if i not in news:
        if index == len(l) - 1:
          news += i
          if len(news) > maxlen:
            maxlen = len(news)
        else:
          news += i
          if len(news) > maxlen:
            maxlen = len(news)
      else:
        news = news[news.index(i)+1:]+i
        print(news)

    return  maxlen

t = Solution()

result = t.lengthOfLongestSubstring("pwwkew")
print(result)

# NOTES:
# Good practices for changing from unmutable to mutable types, deep dive into "for" loop
# Intuition

# Either create all substring = original.pop(0) and iterate through each one
# Or using only original string and iterate through it to find the substring
# Approach

# The first path is too heavy. The code works but not accepted
# The second path:

#     The most important thing is find ways to deal with the similar element when iterating throughout the string. At first, I try to start again by assigning an empty string, but the loop ends right after it goes through the last element of the string. So I wasted lots of time find ways to make the " for " loop continue its operation by using while/while True. But its too heavy to run.
#     I decided to not running away from it :) from there I tried to find the first character of the "news" string, and I got it. Its tricky there, didnt see that at first.
#     Lesson: where you get stuck is where you need to focus on and break through, not running away. Its the key to the solution. In this question, the problem is "cannot find the first character of the substring". So that is the main thing you need to focus on: find the first character of the substring!!
