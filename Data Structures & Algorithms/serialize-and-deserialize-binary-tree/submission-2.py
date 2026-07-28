# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        ans = ""
        queue = deque()
        queue.append([root])
        while queue:
            level = queue.pop()
            temp = []
            for node in level:
                if node == None:
                    ans += "N"
                else:
                    ans += str(node.val)
                    temp.append(node.left)
                    temp.append(node.right)
                ans += "#"
            count = 0
            for i in temp:
                if i==None:
                    count+=1
            if count!=len(temp):
                queue.append(temp)
            ans+="@"
        print(ans)
        return ans

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data=="":
            return None
        i = 0
        queue = deque()
        while i<len(data):
            r = i
            while data[r]!="@":
                r+=1
            l = i
            level = []
            while l<r:
                left = l
                while data[l]!="#":
                    l+=1
                if data[left:l]!="N":
                    node = TreeNode(int(data[left:l]))
                    level.append(node)
                else:
                    level.append(None)
                l= l+1
            i=r+1
                
            queue.append(level)
         
        root = queue.popleft()[0]

        prevL = [root]

        while queue:
            level = queue.popleft()
            i=0
            for node in prevL:
                if node and i+1<len(level):
                    node.left=level[i]
                    node.right=level[i+1]
                    i+=2
            prevL= level
        return root

            
