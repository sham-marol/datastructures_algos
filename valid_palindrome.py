"""

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

-----------------
Runtime : 235 ms , Memory : 16.1 MB
@author : sham-marol

"""

class Solution:
    def isPalindrome(self, strng: str) -> bool:
        
        flag = False
        clist = []
        slist = list(strng.strip().lower())
        invalids = "`,~,!,@,#,$,%,^,&,*,(,),-,_,=,+,<,>,?,/,|,\,[,],{,},:,;,',.,".split(',')
        invalids.append(',')
        invalids.append('''"''')
        invalids.append("")
        invalids.append(" ")
        
        print(invalids)
        
        for i,s in enumerate(slist):
            #print("i:%s | s:%s" % (i,s))
            if s and s not in invalids and s!= '':
                clist.append(s)
      
        str1 = "".join(clist)
        str2 = "".join(list(reversed(str1)))
        
        #print(str1)
        #print(str2)
        
        if str1 == str2:
            flag = True
            
        return flag        
            

        

