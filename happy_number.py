"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
 

Constraints:

1 <= n <= 231 - 1

-------------------------

Runtime : 55 ms , Memory : 14.1 MB
@author : sham-marol

"""

class Solution:
    def isHappy(self, num: int) -> bool:
        
        iters = 0
        numstr = str(num)        
        while True:
            
            summ = 0
            for n in numstr:
                try:
                    summ = summ + pow(int(n),2)                
                except:
                    return False
            print(summ)
            if summ == 1:
                return True
            elif iters > 15 and len(str(summ)) == 1 and summ != 1:
                return False
            elif summ <= 0:
                return False
            
            
            numstr = str(summ)
            iters += 1
            
