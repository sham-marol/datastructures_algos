"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.

-------------------------

Runtime : 67  ms , Memory : 15.3 MB
@author : sham-marol

"""

class Solution:
    def reverseVowels(self, strrng: str) -> str:
        
        vowels = ['a','e','i','o','u','A','E','I','O','U',]
        rstrrng = ""        
        vows = []
        
        lstr = list(strrng)
        for i,s in enumerate(lstr):            
            if s in vowels:
                vows.append(s)
                lstr[i] = "^"
        
        for i,s in enumerate(lstr):            
            if s == "^":                
                lstr[i] = vows.pop()
        
        rstrrng = "".join(lstr)
        return rstrrng
        
      
        
