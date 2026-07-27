# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPathSum = float('-inf')
        def pathsum(root):
            if root==None:
                return 0
            
            leftDepth = pathsum(root.left)
            rightDepth = pathsum(root.right)
            if leftDepth<0:
                leftDepth = max(leftDepth,0)
            if rightDepth<0:
                rightDepth = max(rightDepth,0)
            self.maxPathSum = max(self.maxPathSum, root.val + leftDepth + rightDepth)
            return root.val+max(leftDepth,rightDepth)
        pathsum(root)
        return self.maxPathSum
        