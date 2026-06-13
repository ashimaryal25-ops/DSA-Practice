# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        if root == None:
            return 0
        
        
        if root.left == None and root.right == None:
            return 1

        count1 = self.countNodes(root.right)
        count2 = self.countNodes(root.left)    

        count = count1 + count2

        return count + 1    
        