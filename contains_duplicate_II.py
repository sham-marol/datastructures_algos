"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105

-------------------------

Runtime : 779  ms , Memory : 33.6 MB
@author : sham-marol

"""

import collections

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        return self.approach2(nums,k)
        
    def approach1(self,nums,k): 
        for i in range(len(nums) - 1):
            #klimit = (i + k + 1) if (i + k + 1) < len(nums) else len(nums)
            klimit = (i + k + 1) if (i + k + 1) < len(nums) else (len(nums) )
            klist = nums[i+1:klimit]            
            if nums[i] in klist:
                return True
                    
        return False
    
    
    
    def approach2(self,nums,k):
        
        dictt = defaultdict(list)
        
        for ix,num in enumerate(nums):
            dictt[num].append(ix)
        #print(dictt)
        for ixs in dictt.values():
            if len(ixs) > 1:
                #print(ixs)
                for i in range(len(ixs)-1):
                    #print("%s, %s" % (ixs[i],ixs[i+1]))
                    if abs(ixs[i] - ixs[i+1]) <= k:
                        return True
                    
        return False
