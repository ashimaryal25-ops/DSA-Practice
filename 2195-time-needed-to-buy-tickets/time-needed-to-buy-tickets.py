class Solution(object):
    def timeRequiredToBuy(self, tickets, k):

        queue = deque()
        for i in range(len(tickets)):
            queue.append((i, tickets[i]))
            
        time = 0
        
        while queue:
            person_index, tickets_left = queue.popleft()
            
            tickets_left -= 1
            time += 1
            
            if person_index == k and tickets_left == 0:
                return time
                
            if tickets_left > 0:
                queue.append((person_index, tickets_left))
        
        
        