# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.orders = []

        def dfs(root, depth):
            if not root:
                return None
            
            if depth == len(self.orders):
                self.orders.append([])
            
            self.orders[depth].append(root.val)

            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        
        dfs(root, 0)

        return self.orders

        