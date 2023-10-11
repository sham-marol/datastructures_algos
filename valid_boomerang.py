"""
Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.

A boomerang is a set of three points that are all distinct and not in a straight line.

Example 1:

Input: points = [[1,1],[2,3],[3,2]]
Output: true
Example 2:

Input: points = [[1,1],[2,2],[3,3]]
Output: false
 

Constraints:

points.length == 3
points[i].length == 2
0 <= xi, yi <= 100
-------------------------

Runtime : 68 ms , Memory : 14  MB
@author : sham-marol

"""   

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        
        
        p1=points[0]
        p2=points[1]
        p3=points[2]

        if p1==p2 or p2==p3 or p1==p3:
            return False

        return (p1[0]-p2[0])*(p2[1]-p3[1])!=(p2[0]-p3[0])*(p1[1]-p2[1])

        '''
        xyZCnt = 0
        xZCnt = 0
        yZCnt = 0
        
        xset = set()
        yset = set()
        xyTrue = list()
        xyFalse = list()
        
        for point in points:  
            if point[0] == point[1]:
                xyTrue.append(True)
            else:
                xyFalse.append(False)
            
            if point[0] == 0 and point[1] == 0:
                xyZCnt += 1
            elif point[0] == 0 :
                xZCnt += 1
            elif point[1] == 0 :
                yZCnt += 1
                
            xset.add(point[0])                           
            yset.add(point[1])
       
        
        if len(xyTrue) == 3:
            print("I`m returning it from here - 1")
            return False        
        else :
            if (len(xset) == 1 or len(yset) == 1): 
                print("I`m returning it from here - 2")
                return False
            elif (len(xset) == 2 and len(yset) == 2) and xyZCnt == 1:  
                print("I`m returning it from here - 3")                
                if len(xset - yset) == 0:
                    return True
                return False
            elif (len(xset) == 2 and len(yset) == 2) and ((xZCnt == 2 and yZCnt == 1 ) or (xZCnt == 1 and yZCnt == 2 )): 
                print("I`m returning it from here - 4")
                return False
            #elif (len(xset) == 2 and len(yset) == 2) and len(xyTrue) == 1: 
            #     return True
            print("I`m returning it from here - 5")    
            return True
        
        return True
       '''
