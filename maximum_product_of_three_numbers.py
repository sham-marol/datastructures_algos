"""
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6
 

Constraints:

3 <= nums.length <= 104
-1000 <= nums[i] <= 1000
-------------------------

Runtime : 555 ms , Memory : 15.6 MB
@author : sham-marol

"""   


class Solution:
    
    def maximumProduct(self, nums: List[int]) -> int:
    
        #maxprd =  self.approach1(nums)
        maxprd =  self.approach2(nums)
        
        return maxprd
    
    
    # Brute Force : Time Limit Exceeded Error
    def approach1(self, nums: List[int]) -> int:
        prds = set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i == j or i == k or j == k or i == j == k:
                        continue
                    prd =  nums[i] *  nums[j] *  nums[k]                  
                    prds.add(prd)
                    #print("%s * %s * %s = %s" % (nums[i], nums[j],nums[k],prd))
                    
        return list(sorted(prds)).pop()
        
    
    # Algorithm : Perfect combo + or -
    def approach2(self, nums: List[int]) -> int:
        
        maxprds = []
        pos =  []
        neg = []
        zero = []
               
        for num in nums:
            if num < 0:
                neg.append(num)
            elif num > 0:
                pos.append(num)
            else:
                zero.append(num)
                
        pl = len(pos)      
        nl = len(neg)
        zl = len(zero)
        
        pos = sorted(pos)
        neg = sorted(neg)
        
        #print(pos,neg,zero)
        if pl >= 3:
            maxprds.append(pos[pl-1] * pos[pl-2] * pos[pl-3])
        
        if pl >= 1 and nl >= 2:
            maxprds.append(pos[pl-1] * neg[0] * neg[1])
        
        if  pl >= 2 and nl >= 1:
            maxprds.append(pos[0] * pos[1] * neg[nl -1])
            
        if  nl >= 3:
            maxprds.append(neg[nl-1] * neg[nl-2] * neg[nl-3])
    
        if zl > 0:
            maxprds.append(0)
            
        return list(sorted(maxprds)).pop()
        
            
        
    
    
