# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nonlocal ans, k
            if k == 1:
                ans = node.val
            k -= 1
            if k > 0:
                dfs(node.right)
            
        dfs(root)
        return ans