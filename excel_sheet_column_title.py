"""

Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

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

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"
 

Constraints:

1 <= columnNumber <= 231 - 1

-------------------------

Runtime : 52  ms , Memory : 14 MB
@author : sham-marol

"""

chars = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z".split(",")
class Solution:
    def convertToTitle(self, colnum: int) -> str:
        
        colstr = ""
        
        if colnum < 27:
            colstr = chars[colnum -1]            
        elif int(colnum % 26) != 0 :
            cnum = colnum
            while True:
                mod = int(cnum % 26)
                cnum = int(cnum/26)
                
                if mod == 0:
                    colstr = self.getmod0str(cnum * 26) + colstr
                    print("1 = colstr from mod0: %s" % colstr)
                    break
                else:
                    colstr = colstr + chars[mod-1]
                    print("1 = colstr : %s" % colstr)
                           
                print("1 = cnum : %s | mod : %s" % (cnum,mod))
                                
                
                if  cnum < 27:
                    colstr = colstr + chars[cnum-1]
                    colstr = "".join(reversed(colstr))
                    break
        elif int(colnum % 26) == 0 :
            colstr = self.getmod0str(colnum)
  
        return colstr


    def getmod0str(self,colnum : int):
        colstr = ""
        prevmod0 = False
        cnum = colnum        
        while True:
            mod = int(cnum % 26)
            cnum = int(cnum/26)
            
            print("2 = cnum : %s | mod : %s" % (cnum,mod))
            
            if prevmod0 and mod > 0:
                mod = mod -1
            
            if mod == 0:
                prevmod0 = True
                if cnum < 27:
                    cnum = cnum -1
            colstr = colstr + chars[mod-1]    
            
            if cnum <= 27:
                if cnum == 27:
                    cnum = 26
                colstr = colstr + chars[cnum-1]
                colstr = "".join(reversed(colstr))
                break
                
        return colstr     
    
    
    
            
