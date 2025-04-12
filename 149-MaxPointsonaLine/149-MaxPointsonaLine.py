# Last updated: 4/12/2025, 4:04:19 PM
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:   
        counter = 1
        if len(points) < 2:
            return 1
        for i in range(len(points)):
            egimList = {}
            for j in range(i+1,len(points)):
                y = points[j][1] - points[i][1]
                x = points[j][0] - points[i][0]
                if x != 0:
                    egimList[y / x] = 1 + egimList.get(y / x, 0)
                else:
                    egimList['inf'] = 1 + egimList.get('inf', 0)
            for key,value in egimList.items():
                counter = max(counter,value)
        return counter+1