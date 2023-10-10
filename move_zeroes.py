"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

-------------------------

Runtime : 337 ms , Memory : 15.5 MB
@author : sham-marol

"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = 0
        limit = len(nums)
        while i < limit:
            if nums[i] == 0:
                #print("%s | %s" % (i,nums))                
                nums.append(nums.pop(i))
                #print("%s | %s" % (i,nums))
                limit -= 1
            else:
                i += 1
