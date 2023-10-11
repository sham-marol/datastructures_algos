"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
-------------------------

Runtime : 535 ms , Memory : 14.6 MB
@author : sham-marol

"""   

class Solution:
    def isAnagram(self, word1: str, word2: str) -> bool:
        
        for w in word2:
            if w not in word1:
                return False
            
            word1 = word1.replace(w,"",1)
            
        if word1 != "":
            return False
        
        return True
