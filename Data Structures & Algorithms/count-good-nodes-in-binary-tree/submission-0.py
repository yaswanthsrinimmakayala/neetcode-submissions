# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 1
        def dfs(node,prev):
            if node==None:
                return None
            if node.val>=prev:
                self.count+=1
            prev = max(node.val,prev)
            dfs(node.left,prev)
            dfs(node.right,prev)
        if root:
            if root.left:
                dfs(root.left,root.val)
            if root.right:
                dfs(root.right,root.val)
        return self.count
