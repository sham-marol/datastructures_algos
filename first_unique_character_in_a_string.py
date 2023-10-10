"""

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 
Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.

-------------------------

Runtime : 628  ms , Memory : 14.2 MB
@author : sham-marol

"""

class Solution:
    def firstUniqChar(self, strng: str) -> int:
        
        indnx = -1
        
        checked = []
        for i in range(len(strng)):
            #temp = list(strng)            
            #temp.remove(strng[i])
            #print("%s | %s | %s" % (strng[:i],strng[i],strng[i+1:]))
            
            if strng[i] not in strng[:i] and strng[i] not in strng[i+1:] :
                return i
                      
            
        return indnx

