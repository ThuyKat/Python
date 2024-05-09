class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
    # length of s1 must less than s2
    #  iterate through s2, s2[i] in s1 then left pointer move to that position. windown length = length of s1. check that windown if permutation then return true. if not keep iterating to the end of array. 
    # problem now is how to check permutation quickly. 
        d1 = {}
        s3 =""
        right = 0
        left = 0
        count = 0
        if len(s2)>=len(s1):
            for i in range (0,len(s1)): 
                d1[s1[i]] = d1.get(s1[i],0) +1
            
            for j in range (0,len(s2)):
                print(str(j) +"-"+ s2[j])
                if s2[j] in s1:
                    print(s2[j]) #b
                    count +=1
                    d1[s2[j]] -= 1
                    if  d1[s2[j]] < 0:
                        print("here")
                        
                        d1[s2[j]] +=1
                        print(d1[s2[j]])
                        j+=1
                    left = j
                    right = j+len(s1)-1
                    print("left"+str(left))
                    print("right"+str(right)) #4
                
                elif left < j <= right:
                    
                    print(s2[j])
                    return False
                if count == len(s1):
                    count = 0
                    left = 0
                    right = 0    
                 
                   
            for v in d1.values():
                if v !=0:
                    return False
                    
        if len(s1) > len(s2):
            return False
        return True
s1 = "hello"
s2 = "ooolleoooleh"
solution = Solution()
t = solution.checkInclusion(s1,s2)
print(t)
                
                        
                
            




