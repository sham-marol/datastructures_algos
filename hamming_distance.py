"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.

Example 2:

Input: x = 3, y = 1
Output: 1
 

Constraints:

0 <= x, y <= 231 - 1
-------------------------

Runtime : 51 ms , Memory : 13.8 MB
@author : sham-marol

"""   

import math

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
                
        xbin = list((str(bin(x)).replace('b','')))
        ybin = list((str(bin(y)).replace('b','')))
               
        mxlen = max(len(xbin),len(ybin))        
        lsts = [xbin,ybin]
        
        for lst in lsts:
            while len(lst) != mxlen:
                lst.insert(0,'0')      
                
        #print(xbin,ybin)
        
        hdist = 0
        for i in range(mxlen):
            if xbin[i] != ybin[i]:
                hdist += 1 
        return hdist
