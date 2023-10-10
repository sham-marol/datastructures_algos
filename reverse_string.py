"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.

-------------------------

Runtime : 305  ms , Memory : 18 MB
@author : sham-marol

"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.approach1(s)
        
      
    
    def approach1(self,s):
        '''Aprroach : 1 - Take a list copy to read and edit the original list'''
        
        scpy = s.copy()
        for i in range(len(s)):
            s[i] = scpy.pop()
        
        
    def approach2(self,s):
        '''Aprroach : 2 - In place Soln : Extend the size of the list to hold the elements and pop them to be added back'''
        
        for i in range(len(s)):
            s.append(s[i])
            
        for i in range(int(len(s)/2)):
            s[i] = s.pop()
        
    
    def approach3(self,s):
        '''Aprroach : 3 - In place Soln : Use a temp variable to switch the spots'''
        
        for i,c in enumerate(s):
               
            j = (len(s) - i) - 1    # Cursor from end
            #print("len : %s | i : %s %s| j : %s %s" % (len(s),i,j, s[i],s[j]))
               
            s[i] = s[j]
            s[j] = c
              
            if i == int(len(s)/2) -1 :
                break
       
