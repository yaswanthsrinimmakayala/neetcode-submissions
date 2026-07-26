# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.rootT = None
        i = 0
        def build(preorder,inorder):
            if preorder==[] or inorder==[]:
                return None
            if preorder[0] in inorder:
                indx = inorder.index(preorder[0])
            else:
                return None
            if self.rootT==None:
                self.rootT = TreeNode(inorder[indx])
                root = self.rootT
            else:
                root = TreeNode(inorder[indx])
            count = len(inorder[:indx])
            root.left = build(preorder[1:count+1],inorder[:indx])
            root.right = build(preorder[1+count:],inorder[indx+1:])
            return root
        build(preorder,inorder)
        return self.rootT