class Solution(object):
    def deckRevealedIncreasing(self, deck):
        n = len(deck)

        deck.sort()
    
        res = [0] * n 
        
        queue = deque(range(n)) 

        for card in deck:
            reveal_index = queue.popleft()
            
            res[reveal_index] = card
            
            if queue:
                next_index = queue.popleft()
                queue.append(next_index)
                
        return res


              
        