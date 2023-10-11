"""
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false
 

Constraints:

1 <= s.length, goal.length <= 100
s and goal consist of lowercase English letters.

-------------------------

Runtime : 59 ms , Memory : 13.8 MB
@author : sham-marol

"""

class Solution:
    def rotateString(self, strng: str, goal: str) -> bool:
        
        rtstrng = strng
        for i in range(len(strng)):
            
            rtstrng = rtstrng[1:len(rtstrng)] + rtstrng[0]
                        
            if rtstrng == goal:
                return True
            
        return False

