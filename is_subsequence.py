"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

-------------------------

Runtime : 70  ms , Memory : 14  MB
@author : sham-marol

"""

class Solution:
    def isSubsequence(self, substrr: str, strr: str) -> bool:
        
        if substrr == "":
            return True
        
        flag = False        
        ls_substrr1 = list(substrr)  
        ls_substrr2 = list()
        
        sb = ls_substrr1.pop(0)
        
        for s in strr:
            if s == sb:
                ls_substrr2.append(s)
                try:
                    sb = ls_substrr1.pop(0)
                except:
                    pass
              
        
        if substrr == "".join(ls_substrr2):
            flag = True
            
        return flag
