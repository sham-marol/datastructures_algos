"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.

-------------------------

Runtime : 55 ms , Memory : 14.2 MB
@author : sham-marol

"""

import collections

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        isomap1 = defaultdict(set)
        isomap2 = defaultdict(set)
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            isomap1[s[i]].add(t[i])
        for i in range(len(s)):        
            isomap2[t[i]].add(s[i])
            
        for k,vals in isomap1.items():
            if len(vals) > 1:
                return False 
        for k,vals in isomap2.items():
            if len(vals) > 1:
                return False 
            
        return True
        
        
def main():
    pass

if __name__ == '__main__':
    main()
