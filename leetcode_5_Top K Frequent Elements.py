# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]



class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        distint = set(nums) # the set contains all distinct value of nums
        my_dict ={}
        # create a dictionary with keys are elements of set( or distinct value of nums array), values are frequencies of them in nums. 
        for i in distint:
            my_dict[i] = nums.count(i)
        
        # sort a dictionary accoring to its value
        sort =  sorted(my_dict.items(), key=lambda x: x[1], reverse = True)
        sorted_dict = dict(sort)
        # return the k elements with the highest values from sorted_dict:
        output = list(sorted_dict.keys())[0:k]
        
        return output