"""
Given an integer x, return true if x is a palindrome , and false otherwise.
Runtime : 55 ms , Memory : 13.2 MB
@author : sham-marol
"""

class Solution(object):
    def isPalindrome(self, num):
        """
        :type x: int
        :rtype: bool
        """
        res = False
        numst1 = str(num)        
        numst2 =  numst1[::-1]
        if numst1 == numst2:
            res = True       
        return res      
        
