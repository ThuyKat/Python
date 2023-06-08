# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
class Solution:
 
  def twoSum(self,nums,target):
    
    result =[]
    for  index, x in enumerate (nums):
      y = target -x
      if y in nums :
        if nums.index(y) != index: 
          result.append(index)
          result.append(nums.index(y))
          break
        
        
          
    return result
  #NOTES:
# 1) .index method only returns the index of the first matching value, so its impossible to use nums.index(x) != nums.index(y) as a condition to filter y
# This leads to the use of enumerate
# 2) Its important to break the condition 1: y in nums and the condition 2: nums.index(y) != index into 2 ifs. This is because we only want to consider only y in the list, not y outside the list. 
# 3) " break" is important to end the loop on the first x and y found, so the result wont continue and adding the second y and second x 