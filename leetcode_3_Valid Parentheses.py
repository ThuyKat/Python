# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

 

# Example 1:

# Input: s = "()"
# Output: true

class Solution(object):
    
  def isValid(self, s):
    mode = ["()", "{}", "[]"]
    open = ["(","{","["]
    # check string is created to validate the completeness of the bracket pairs
    check = ""
    for i in range(0,len(s)): 
    # if it is open bracket, add it to the check string
      if s[i] in open: 
        check += s[i]
    # if it is close bracket, test if it forms a pair with the last open bracket we added to the check string. 
      else:
        if len(check)>0:
        # if it froms a pair, exclude the last open bracket from the check string
            if check[-1] + s[i] in mode:
                check = check[:-1]
        # if it doesnt from a pair, return False
            else:
                return False 
        # if we found a close bracket and the check string is empty, return False
        else:
            return False  
    # At the end of the loop, see if length of the check string is equal to 0, if it's equal, return True
    if len(check) == 0:
      return True
    # if after going through the string the check string still contains unmatch bracket, return False
    else:
      return False
