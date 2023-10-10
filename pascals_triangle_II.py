"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33

-------------------------

Runtime : 54 ms , Memory : 13.9 MB
@author : sham-marol

"""

class Solution:
    def getRow(self, rowindx: int) -> List[int]:
        
        pascal = []        
        i = 0               # row index
        while True:
            row = []
            
            if i == 0:
                row = [1]    
            elif i == 1:
                row = [1,1]
            else:
                prow = pascal[i-1]              # Previous Row
                for j in range(len(prow)-1):
                    row.append(prow[j] + prow[j+1])
                row = [prow[0]] + row + [prow[len(prow)-1]]                                   
            pascal.append(row)
            
            if i == rowindx:
                return pascal[i]
            i += 1
            
def main():
    pass

if __name__ == '__main__':
    pass

