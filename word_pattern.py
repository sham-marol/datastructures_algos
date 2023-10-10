"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
 

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.

-------------------------

Runtime : 59  ms , Memory : 13.9 MB
@author : sham-marol

"""

import collections

class Solution:
    def wordPattern(self, pattern: str, sentc: str) -> bool:
        
        c2wrd = defaultdict(set)
        words = sentc.split(' ')
        
        if len(pattern) != len(words):
            return False
        
        for i in range(len(pattern)):
            c2wrd['c-'+ pattern[i]].add(words[i])
            c2wrd['w-'+ words[i]].add(pattern[i])
            
        #print(c2wrd)
        
        for vals in c2wrd.values():
            if len(vals) > 1:
                return False
            
        return True
        
