"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30

-------------------------

Runtime : 67 ms , Memory : 14 MB
@author : sham-marol

"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        tlist = []
        for i in range(1,numRows+1):
            rlist = []
            if i == 1:
                rlist = [1]
            elif i == 2:
                 rlist = [1,1]
            else:
                plist = tlist[i-2]
                
                for j in range(len(plist) - 1):
                    rlist.append(plist[j] + plist[j+1])
                rlist.insert(0,plist[0])
                rlist.insert(len(rlist),plist[len(plist)-1])
            tlist.append(rlist)
        
        return tlist

                
