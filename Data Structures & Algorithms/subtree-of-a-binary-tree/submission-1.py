# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(one, two):
            if not one and not two:
                return True
            
            if not one or not two:
                return False
            
            if one.val != two.val:
                return False
            
            return (isSameTree(one.left, two.left) and isSameTree(one.right, two.right))
        
        if not root:
            return False
        
        if isSameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
            

        