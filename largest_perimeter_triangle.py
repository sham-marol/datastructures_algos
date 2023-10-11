"""
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

Example 1:

Input: nums = [2,1,2]
Output: 5
Explanation: You can form a triangle with three side lengths: 1, 2, and 2.

Example 2:

Input: nums = [1,2,1,10]
Output: 0
Explanation: 
You cannot use the side lengths 1, 1, and 2 to form a triangle.
You cannot use the side lengths 1, 1, and 10 to form a triangle.
You cannot use the side lengths 1, 2, and 10 to form a triangle.
As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.
 

Constraints:

3 <= nums.length <= 104
1 <= nums[i] <= 106
-------------------------

Runtime : 205  ms , Memory : 15.3 MB
@author : sham-marol

""" 

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        sides = list(reversed(sorted(nums)))
        
        per = 0
        while len(sides) >= 3:             
            
            if (sides[1] + sides[2]) > sides[0]:
                per = sides[0] + sides[1] + sides[2]
                return per
            sides.pop(0)
        return 0
                    
