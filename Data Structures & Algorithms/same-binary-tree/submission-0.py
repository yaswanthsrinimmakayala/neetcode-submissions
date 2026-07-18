# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if q==None and p==None:
            return True
        if (q!=None and p==None) or (q==None and p!=None):
            return False
        if p and q and p.val!=q.val:
            return False
        l = self.isSameTree(p.left, q.left)
        e = self.isSameTree(p.right,q.right)
        return l and e