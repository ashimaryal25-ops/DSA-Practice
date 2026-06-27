class Solution(object):
    def checkInclusion(self, s1, s2):
        
        map1 = {}
        for s in s1:
            if s in map1:
                map1[s] += 1
            else:
                map1[s] = 1    


        if len(s2) < len(s1):
            return False
        left = 0
        right = len(s1)

        windowMap = {}

        #mapping initial window

        for i in range( right ):

            if s2[i] in windowMap:
                windowMap[s2[i]] += 1

            else:
                windowMap[s2[i]] = 1    

        if  windowMap == map1:
            return True

        for i in range( right, len(s2) ):

            windowMap[s2[left]] -= 1

            if windowMap[s2[left]] == 0:
                windowMap.pop(s2[left])

           

            if s2[right] in windowMap:
                windowMap[s2[right]] += 1
            else:    
                windowMap[s2[right]] = 1

            left += 1

            right += 1

            if windowMap == map1:
                return True    
        
        return False

            
            
