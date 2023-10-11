"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:

Input: nums = [1,1]
Output: [2]
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n

-------------------------

Runtime : 713 ms , Memory : 26.8 MB
@author : sham-marol

""" 

class Solution:
    
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        return self.appoach1(nums)
        #return self.appoach2(nums)
    
    
    def appoach1(self, nums: List[int]) -> List[int]:
        
        expected = [i for i in range(1,len(nums) +1)]
        return set(expected) - set(nums)
        
    '''
    def appoach2(self, nums: List[int]) -> List[int]:
        
        prev = 0
        dispeard = []
        nums = list(set(sorted(nums)))
        for n in :
            if n != i:
                dispeard.append(cnt)
                
     '''          
