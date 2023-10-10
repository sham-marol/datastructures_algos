"""

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
-------------------------

Runtime : 33  ms , Memory : 13.8 MB
@author : sham-marol

"""

"""
__author__ = sham.marol
The logic is same as Fibonacci series : 0,1,1,2,3,5,8,13...
"""

class Solution:
    def climbStairs(self, n: int) -> int:
       
        a = 0
        b = 1
        
        i = 1
        while True:            
            c = a + b            
            a = b
            b = c
            
            if i == n:
                return c
            
            i += 1
