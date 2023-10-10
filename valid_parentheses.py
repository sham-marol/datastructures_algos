"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

Runtime 5625 ms , Memory : 13.6 MB
@author : sham-marol
"""

o2c = { '(':')','{':'}','[':']' }
c2o = { ')':'(','}':'{',']':'[' }
    
class Solution(object):
            
    def isValid(self, strs):
        """
        :type s: str
        :rtype: bool
        """
       
        flag = True
        opens = closed =  []
        
        strs = self.remove(list(strs))
        i = 0
        while i < len(strs):        
            if strs[i] in o2c.keys():
                opens.append(strs[i])                
            elif strs[i] in o2c.values():
                if c2o.get(strs[i]) not in opens:
                    return False
                closed.append(strs[i])
                
            i += 1    
            
        print("Opens : %s" % opens)
        print("Closed : %s" % closed)
        
        if len(opens) != len(closed):
            return False
        
        rclosed = list(reversed(closed))
        x = 0 
        while x < len(opens):
            print("opens[x]  : %s" % opens[x])
            print("closed[x] : %s" % rclosed[x])
            if o2c.get(opens[x]) != rclosed[x]:                
                print("Why im here : %s = %s" % (o2c.get(opens[x]),rclosed[x]))
                return False
            x +=1
            
        return flag
      
        
    def remove(self, strs):
        for k in range( int(len(strs)/2)):
            i = 0
            while i < len(strs):
                if (i != len(strs)-1) and (o2c.get(strs[i]) == strs[i+1]):                    
                    strs.pop(i)
                    strs.pop(i)
                    i += 2
                i += 1
        print("Removed : %s" % strs)
        return strs

        





