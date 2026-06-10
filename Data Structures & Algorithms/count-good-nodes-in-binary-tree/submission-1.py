# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.goods = 0

        def dfs(root, prev):

            if not root:
                return None
            
            if root.val >= prev:
                self.goods += 1
            
            current_max = max(root.val, prev)

            dfs(root.left, current_max)
            dfs(root.right, current_max)
        
        dfs(root, -9999999999)

        return self.goods
        