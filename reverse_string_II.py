"""
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:

Input: s = "abcd", k = 2
Output: "bacd"
 

Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 104

-------------------------

Runtime : 49 ms , Memory : 14.1 MB
@author : sham-marol

"""

class Solution:
    def reverseStr(self, strng: str, k: int) -> str:
        
        revstr = ""
        for i in range(0,len(strng),(2 * k)):
            j = i + (2 * k)
            substr = strng[i:j]
            rsubstr = "".join(list(reversed(substr[0:k]))) + substr[k:len(substr)]
            revstr += rsubstr
                   
        return revstr
            
            
            
