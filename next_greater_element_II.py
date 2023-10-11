"""
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.

Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
 

Constraints:

1 <= nums.length <= 104
-109 <= nums[i] <= 109
-------------------------

Runtime : 9315 ms , Memory : 15.4 MB
@author : sham-marol

"""   

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        res = []        
        for i in range(len(nums)):         
            
            grt = None
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    grt = nums[j]
                    break
                    
            if grt is None:
                for k in range(i+1):
                    if nums[k] > nums[i]:
                        grt = nums[k]
                        break 
                        
            if grt is None:
                grt = -1
                
            res.append(grt)
        return res
            
