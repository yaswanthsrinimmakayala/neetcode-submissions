# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        queue = deque()
        queue.append([root])
        result = [root.val]
        while queue:
            level = queue.popleft()
            l = []
            while level:
                node = level.pop(0)
                if node.left:
                    l.append(node.left)
                if node.right:
                    l.append(node.right)
            if l:
                queue.append(l)
                result.append(l[-1].val)
        return result