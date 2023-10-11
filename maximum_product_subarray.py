"""
Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
-------------------------

Runtime : 165 ms , Memory : 14.8 MB
@author : sham-marol

"""   

import collections

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxprds = []
                
        if 0 in nums and len(nums) > 1:
            numlsts = self.splitlist(nums,0)
        else:
            numlsts = [nums]
        
        print(numlsts)
        for numlst in numlsts:
            if len(numlst) == 0:
                continue
            neginx = []
            for i in range(len(numlst)):
                if numlst[i] < 0:
                    neginx.append(i)
            
            # If negs are even, then multiply all as the product will be +ve & greater          
            if len(neginx) % 2 == 0:
                prd = 1
                for n in numlst:
                    prd *= n
                maxprds.append(prd)
            else:   # If negs are odd, then get sublists so that -ves are even and get the products
                numcpys = []
                
                if len(numlst) == 1:
                    numcpys.append(numlst)
                else:
                    inx1 = neginx.pop(0)
                    numcpys.append(numlst[inx1+1:])
                    try:                    
                        inxN =neginx.pop()                    
                    except:
                        inxN = inx1
                    numcpys.append(numlst[:inxN])
              
                for numcpy in numcpys:
                    if len(numcpy) == 0:
                        continue
                  
                    prd = 1
                    for n in numcpy:
                        prd *= n
                    maxprds.append(prd)

        return list(sorted(maxprds)).pop()
    
    
    def splitlist(self,nums:List[int],delm:int) -> List[List[int]]:
        numlsts = []
        sublst = nums
                
        if delm in nums:
            numlsts.append([delm])
        
        while delm in sublst:
            ix = sublst.index(delm)
            numlsts.append(sublst[:ix])
            sublst = sublst[ix+1:] 
            #print("Here - %s" % sublst)
        if len(sublst) > 0:
            numlsts.append(sublst)
            
        return numlsts
                
  
