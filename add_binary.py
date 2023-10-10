"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

-------------------------
Binary Addition  | Decimal Conversion
0 + 0 = 0        |      
1 + 0 = 1
0 + 1 = 1
1 + 1 = 10       | 1 *2^1 + 1 * 2^0 = 3

Runtime : 108 ms , Memory : 14 MB
@author : sham-marol

"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        mxlen = max(len(a),len(b))
        
        sumstr = ""                                                  
        carr = [0] * mxlen                           
        ic = ( mxlen - 1)      
        
        
        ia = len(a) - 1                                   
        ib = len(b) - 1

        while True:                                  
            aa = bb = s = 0

            if ia > -1 and ia < len(a) :                   
                aa = int(a[ia]) 
            if ib > -1 and ib < len(b)  :
                bb = int(b[ib]) 

            s  = aa + bb + carr[ic]                    
            #print("s: %s = aa:%s + bb:%s + carr[ic]:%s" % (s,aa, bb, carr[ic]))
            
            if s == 2:
                s = "10"
                
                if ic != 0:
                    s = "0"
                    carr[ic-1] = 1   
                    
            elif s == 3:
                s = "11"                
                if ic != 0:
                    s = "1"
                    carr[ic-1] = 1  
            
            sumstr = str(s) + sumstr
            print("ic : %s | %s" % (ic,carr))
            print("ia : %s | %s" % (ia,a))
            print("ib : %s | %s" % (ib,b))
            print(sumstr)

            if ia <= 0 and ib <= 0:
                break
                
            ia -= 1
            ib -= 1
            ic -= 1
            print("ib:%s" % ib)
        return sumstr     
            
        
def main():
    pass
    
if __name__ == '__main__':
    main()
                
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                
            
                
