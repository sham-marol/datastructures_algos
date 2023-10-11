"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 
Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
-------------------------

Runtime : 78  ms , Memory : 14.2 MB
@author : sham-marol

"""   

class Solution:
    
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        return self.aproach1(ransomNote,magazine)
    
    
    def aproach1(self, ransomNote: str, magazine: str) -> bool:
        for r in ransomNote:
            #print("%s | %s" % (r,magazine))
            if r not in magazine:
                return False
            magazine = magazine.replace(r,"",1)

        return True
    
    
    def aproach2(self, ransomNote: str, magazine: str) -> bool:
        for r in ransomNote:
            if ransomNote.count(r) >  magazine.count(r):
                return False
        return True
