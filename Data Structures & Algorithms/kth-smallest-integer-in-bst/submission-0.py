# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        ints = []

        def dfs(root):
            if not root:
                return None
            
            dfs(root.left)
            ints.append(root.val)
            dfs(root.right)
        
        dfs(root)
        return ints[k-1]
            

        