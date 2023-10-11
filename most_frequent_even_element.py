"""
Given an integer array nums, return the most frequent even element.

If there is a tie, return the smallest one. If there is no such element, return -1.


Example 1:

Input: nums = [0,1,2,2,4,4,1]
Output: 2
Explanation:
The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.
Example 2:

Input: nums = [4,4,4,9,2,4]
Output: 4
Explanation: 4 is the even element appears the most.
Example 3:

Input: nums = [29,47,21,41,13,37,25,7]
Output: -1
Explanation: There is no even element.
 

Constraints:

1 <= nums.length <= 2000
0 <= nums[i] <= 105
-------------------------

Runtime : 1375 ms , Memory : 14.3 MB
@author : sham-marol

"""

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        
        
        cnt2nums = defaultdict(list)
        
        for n in nums.copy():
            if (n % 2 != 0):  # IF not even, then del
                nums.remove(n)
        
        if len(nums) == 0:
            return -1
        
        processed = set()    
        
        for n in nums:
            if n not in processed:
                cnt2nums[nums.count(n)].append(n)
            processed.add(n)
        
        cnts = cnt2nums.keys()
        bigcnt = list(sorted(cnts))[len(cnts)-1]
        
        nums = cnt2nums.get(bigcnt)
        
        return list(sorted(nums))[0]

        
