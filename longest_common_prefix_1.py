"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Runtime : 53 ms , Memory : 13.9 MB
@author : sham-marol
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        cprefix = ""
        if len(strs) == 0:
            raise Exception("No stings passed")            
        st1 = strs[0]
        
        for i in range(len(st1)):
            flag = True
            prfx = st1[0:i+1]
                
            for ix,st in enumerate(strs):
                                                   
                if not st.startswith(prfx):
                    flag = False
                    print("i:prfx : string = %s:%s:%s" % (i,prfx,st))
            
            if flag == True:
                cprefix = prfx                            
                
        return cprefix
