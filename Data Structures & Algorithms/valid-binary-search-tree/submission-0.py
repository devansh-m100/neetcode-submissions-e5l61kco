# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # O(n) time | O(n) space, where n is the number of nodes in the BST
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, lowerBoundVal, upperBoundVal):
            if not node:
                return True
            if not (node.val > lowerBoundVal and node.val < upperBoundVal):
                return False
            return valid(node.left, lowerBoundVal, node.val) and valid(node.right, node.val, upperBoundVal)
        return valid(root, float("-inf"), float("inf"))
        