# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.maxsum = root.val

        def dfs(root):

            if not root:
                return 0
            
            leftmax = max(dfs(root.left), 0)
            rightmax = max(dfs(root.right), 0)

            total = root.val + leftmax + rightmax

            self.maxsum = max(self.maxsum, total)

            return root.val + max(leftmax, rightmax)
        
        dfs(root)
        
        return self.maxsum
        