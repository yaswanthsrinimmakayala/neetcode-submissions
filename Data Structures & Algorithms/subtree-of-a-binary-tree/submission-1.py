# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def isSameTree(self,root1,root2):
        if root1==None and root2==None:
            return True
        if root1!=None and root2==None:
            return False
        if root1==None and root2!=None:
            return False
        if root1.val!=root2.val:
            return False
        l = self.isSameTree(root1.left,root2.left)
        r = self.isSameTree(root1.right,root2.right)
        return l and r
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root ==None:
            return False
        if self.isSameTree(root,subRoot):
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
