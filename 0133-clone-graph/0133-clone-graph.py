class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None
            
        old_to_new = {} # Our translation ledger
        
        def clone(node):
            # Base Case: Have we already cloned this node?
            if node in old_to_new:
                return old_to_new[node] # returnthe existing clone
                
            # Build the Clone
            copy = Node(node.val)
            old_to_new[node] = copy # IMMEDIATELY save it to the map
            
            # Explore and wire up the neighbors
            for neighbor in node.neighbors:
                # Recursively clone the neighbor, then append it to copy's list
                copy.neighbors.append(clone(neighbor))
                
            return copy
            
        return clone(node)
        