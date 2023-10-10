"""
Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

Example 1:

Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
Example 2:

Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
 
Constraints:

1 <= num <= 231 - 1

-------------------------

Runtime : 1038 ms , Memory : 15.9 MB
@author : sham-marol

"""

import collections

class Solution:
    
    def isPerfectSquare(self, num: int) -> bool:        
      
        flag = False
        sq = 1
        i = 2
        squares = []
        
        max = pow(2,31) - 1
        
        while sq <  max:
            squares.append(sq)
            sq = i * i
            i += 1
        
        if  num in squares:
            flag = True
            
        return flag
    
              
