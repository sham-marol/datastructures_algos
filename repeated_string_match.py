"""
Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. If it is impossible for b​​​​​​ to be a substring of a after repeating it, return -1.

Notice: string "abc" repeated 0 times is "", repeated 1 time is "abc" and repeated 2 times is "abcabc".

Example 1:

Input: a = "abcd", b = "cdabcdab"
Output: 3
Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.

Example 2:

Input: a = "a", b = "aa"
Output: 2
 
Constraints:

1 <= a.length, b.length <= 104
a and b consist of lowercase English letters.
-------------------------

Runtime : 67  ms , Memory : 13.9 MB
@author : sham-marol

"""   

import math
class Solution:
    def repeatedStringMatch(self, aString: str, bString: str) -> int:
        times = math.ceil(len(bString) / len(aString))
        for i in range(2):
            if bString in (aString * (times + i)):
                return (times + i)
        return -1        
        
