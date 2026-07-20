class Solution:
    def findRedundantConnection(self, edges):
        #Setup the parent array. Everyone points to themselves initially.
        parent = [i for i in range(len(edges) + 1)]
        
        # Keep checking the array until a node points to itself.
        def find(n):
            if parent[n] == n:
                return n
            return find(parent[n]) # Recursively climb up the chain
            
        # The Union Engine: Connect two nodes if they aren't already.
        def union(n1, n2):
            p1 = find(n1) # Find the top of n1's chain
            p2 = find(n2) # Find the top of n2's chain
            
            if p1 == p2:
                return False # cycle detected. They are already in the same chain.
                
            # Connect them by making p1 point to p2
            parent[p1] = p2 
            return True
            
        #  Feed the edges into the engine
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2] # Return the exact edge that caused the cycle