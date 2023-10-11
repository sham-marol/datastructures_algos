"""
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:

Input: s = "aba"
Output: false

Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 
Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
-------------------------

Runtime : 1316  ms , Memory : 14 MB
@author : sham-marol

"""

class Solution:
    def repeatedSubstringPattern(self, strr1: str) -> bool:
        
        for i in range(1,len(strr1)):
            sbstr = strr1[0:i]  
            strr2 = sbstr * round(len(strr1)/len(sbstr))
            if strr2 == strr1:
                return True
        return False
            
            
            
