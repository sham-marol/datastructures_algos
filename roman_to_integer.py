"""
Given a roman numeral, convert it to an integer. Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Runtime : 130 ms , Memory : 13.5 MB
@author : sham-marol
"""

class Solution(object):
    def romanToInt(self, romstr):
        """
        :type s: str
        :rtype: int
        """
              
        r2i = { 'I': 1 , 'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
               
        isum = 0
        ix = len(romstr) - 1
        r1 = r2 = ''
        while ix > -1 :        
            r2 = romstr[ix]
            if ix != 0 :
                r1  = romstr[ix-1]
                        
            i = r2i.get(r1+r2,0)
            if i == 0:
                i = r2i.get(r2)                
                ix -= 1
                print("%s:%s | %s" % (r2,i,ix))
            else:
                ix -= 2
                print("%s:%s | %s" % ((r1+r2),i,ix))
            isum += i
            r1 = r2 = ''
        return isum
    
