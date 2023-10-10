"""
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 
Example 1:

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701
 

Constraints:

1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].

-------------------------

Runtime : 54 ms , Memory : 13.9 MB
@author : sham-marol

"""

alphas = "_,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z".split(',')

class Solution:
    
    coln = 0
    
    def titleToNumber(self, ct: str) -> int:
       
        if len(ct) == 1:
            return alphas.index(ct)
        
        return self.getcoln(ct)
    
    
    def getcoln(self,ct: str) -> str:
        
        if len(ct) == 2: 
            return (26 * alphas.index(ct[0])) + alphas.index(ct[1])
        else:
            return (26 * self.getcoln(ct[:len(ct)-1])) + alphas.index(ct[len(ct)-1]) 
        
def main():
    #print(alphas[:len(alphas)-1])
    pass

if __name__ == '__main__':
    main()
        
