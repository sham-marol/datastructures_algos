"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

 

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false
 

Constraints:

-231 <= n <= 231 - 1

-------------------------

Runtime : 56  ms , Memory : 13.9 MB
@author : sham-marol

"""

class Solution:
    
    def isPowerOfTwo(self, n: int) -> bool:
        return self.approach1(n)
        
    # Check if pow(2,i) == n
    def approach1(self,n):
                   
        i = 0
        while True:
            if pow(2,i) == n:
                return True 
            elif pow(2,i) > n < pow(2,(i+1)) :
                return False
                
            i += 1
            
        return flag
    
def main():
    pass

if __name__ == '__main__':
    main()
        
