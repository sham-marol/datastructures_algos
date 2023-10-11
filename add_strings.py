"""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"
 

Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
-------------------------

Runtime : 61 ms , Memory : 14.5 MB
@author : sham-marol

"""   

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        summ = self.apprch2(num1,num2)
        #summ = self.apprch1(num1,num2)
    
        return summ
    
    
    
    # Traditional : str to int conversion
    def apprch1(self, num1: str, num2: str) -> str:
        iNum1 = int(num1)
        iNum2 = int(num2)
        
        summ = iNum1 + iNum2
        
        return str(summ)
    
    
    
    def apprch2(self, num1: str, num2: str) -> str:
        nums1 = list(num1)
        nums2 = list(num2)
        res, carry = [], 0

        while nums1 or nums2:
            n1 = n2 = 0
            if nums1: n1 = ord(nums1.pop()) - ord('0')
            if nums2: n2 = ord(nums2.pop()) - ord('0')
            
            carry, remain = divmod(n1 + n2 + carry, 10)
            res.append(remain)
        
        if carry:
            res.append(carry)
            
        return ''.join(str(d) for d in res)[::-1]
