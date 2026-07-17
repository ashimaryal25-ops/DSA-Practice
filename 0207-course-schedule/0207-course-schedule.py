from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        unlocks = {i: [] for i in range(numCourses)}
        locks = [0] * numCourses
        
        for course, prereq in prerequisites:
            unlocks[prereq].append(course)
            locks[course] += 1
            
        q = deque()
        for i in range(numCourses):
            if locks[i] == 0:
                q.append(i)
                
        classes_passed = 0
        
        while q:
            curr = q.popleft()
            classes_passed += 1
            
            for next_course in unlocks[curr]:
                locks[next_course] -= 1
                
                if locks[next_course] == 0:
                    q.append(next_course)
                    
        return classes_passed == numCourses