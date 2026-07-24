# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        in_order = []
        def inorder(root):
            if root==None:
                return None
            inorder(root.left)
            in_order.append(root.val)
            inorder(root.right)
        inorder(root)
        print(in_order)
        for i in range(1,len(in_order)):
            if in_order[i]<=in_order[i-1]:
                return False
        return True
