"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 
Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
-------------------------

Runtime : 382 ms , Memory : 15.1 MB
@author : sham-marol

"""   

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        numstrs = "".join([str(n) for n in nums]).split('0')
        
        oneslen = []
        for num in numstrs:
            oneslen.append(len(num))
        
        return max(oneslen)
            
