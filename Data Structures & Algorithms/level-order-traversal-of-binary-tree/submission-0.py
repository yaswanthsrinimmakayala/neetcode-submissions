# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = [[root]]
        while queue:
            temp = []
            level = queue.pop(0)
            l = []
            while level:
                node = level.pop(0)
                if node:
                    temp.append(node.val)
                    if node.left:
                        l.append(node.left)
                    if node.right:
                        l.append(node.right)
            if l:
                queue.append(l)
            if temp:
                result.append(temp)
        return result
