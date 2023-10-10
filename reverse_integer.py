"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1

-------------------------

Runtime : 38  ms , Memory : 13.9 MB
@author : sham-marol

"""

class Solution:
    def reverse(self, x: int) -> int:
        
        revs = ""
        
        if x < 0:           
            x = str(x).strip('-')   
            revs = "".join(list(reversed(str(x))))            
            revs = "-" + revs
        else:    
            revs = "".join(reversed(str(x)))
        
        num = int(revs)
        
        if num < (-(pow(2,31))) or num > (pow(2,31)-1):
            num = 0
            
        return num


        
def main():
    '''
    pass
    num = 2147483649
    
    if num < (-(pow(2,31))) or num > (pow(2,31)-1):
        print("OO range")
    else:
        print("In range")
    '''


if __name__ == '__main__':
    main()
