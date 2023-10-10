"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

Constraints:

1 <= s.length <= 2000

-------------------------

Runtime : 78 ms , Memory : 14 MB
@author : sham-marol

"""

class Solution:
    def longestPalindrome(self, sttring: str) -> int:
        
        single = 0
        partners = {}
        longest = 0
        
        for st in sttring:
            cnt = partners.get(st,0)            
            partners[st] = cnt + 1
        
        print(partners)
        for st,cnt in partners.items():
                       
            if (cnt % 2 == 0 ) :
                longest += cnt
                print("%s | %s | %s" % (st,cnt,longest))                          
            elif (cnt > 1 and single == 0):
                single = 1
                longest += cnt
                print("%s | %s | %s" % (st,cnt,longest))
            elif (cnt > 1 and single != 0):
                longest += cnt - 1
                print("%s | %s | %s" % (st,cnt,longest))
            elif (cnt == 1 and single == 0):
                single = 1
                longest += single
                print("%s | %s | %s" % (st,single,longest))
            
        return longest
                
