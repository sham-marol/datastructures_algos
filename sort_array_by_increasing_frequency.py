"""
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.


Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
Example 2:

Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
Example 3:

Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]
 

Constraints:

1 <= nums.length <= 100
-100 <= nums[i] <= 100
-------------------------

Runtime : 112 ms , Memory : 13.8 MB
@author : sham-marol

"""   

import collections

class Solution:
    
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        freqncy = []
        
        num2lst = defaultdict(list)
        len2lst = defaultdict(list)
        
        for num in nums:
            num2lst[num].append(num)
            
        srteds = sorted(num2lst.values(),key=len)
        #print(srteds)
        
        for srted in srteds:
            len2lst[len(srted)].append(srted)
        
        for lenn in sorted(len2lst.keys()):
            
            lsts = len2lst.get(lenn)
            
            if len(lsts) > 1:                
                lsts = sorted(lsts)
            #print(lsts)
            
            for i in range(len(lsts)-1,-1,-1):
                freqncy.extend(lsts[i])   
                    
        return freqncy
