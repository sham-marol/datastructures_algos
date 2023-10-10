"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.


Example 1:

Input: n = 27
Output: true
Explanation: 27 = 33
Example 2:

Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.
Example 3:

Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1).
 

Constraints:

-231 <= n <= 231 - 1
 
-------------------------

Runtime : 84 ms , Memory : 14 MB
@author : sham-marol

"""

class Solution:
    def isPowerOfThree(self, num: int) -> bool:
        
        if num <= 0:
            return False
        
        return self.approach1(num)
        
    
    # Check if its divisible by 3 all the way till 1    
    def approach1(self,num):
        
        while (num % 3) == 0:
            num = num/3
            #print(int(num))
            
        return int(num) == 1

    
    # Brute force : iterate i and use pow(3,i)
    def approach2(self,num):
        
        for i in range(pow(2,31)-1): 
            
            if pow(3,i) == num:
                return True
            elif pow(3,i) > num:
                return False
        
           
