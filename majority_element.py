"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

-------------------------

Runtime : 171 ms , Memory : 15 MB
@author : sham-marol

"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n2count = {}
        for n in nums:
            
            cntX = n2count.get(n,0)
            n2count[n] = cntX + 1
            
        
        for n, cnt in n2count.items():
            if cnt > int(len(nums)/2):
                return n
            
