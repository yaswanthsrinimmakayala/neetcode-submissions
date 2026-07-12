class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.lru = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    def move_to_end(self,Node):
        left = Node.prev
        right = Node.next
        left.next = right
        right.prev = left
        temp = self.right
        pre = self.right.prev
        pre.next = Node
        Node.next = temp
        temp.prev = Node
        Node.prev = pre
        self.right = temp
    def get(self, key: int) -> int:
        if key in self.lru.keys():
            self.move_to_end(self.lru[key])
            return self.lru[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self.lru[key].val = value
            self.move_to_end(self.lru[key])
        else:
            if len(self.lru)>=self.size:
                temp = self.left.next
                self.left.next = temp.next
                temp.next.prev = self.left
                del self.lru[temp.key]
            
            self.lru[key] = Node(key,value)
            temp = self.right
            pre= self.right.prev
            pre.next = self.lru[key]
            self.lru[key].next = temp
            self.lru[key].prev =  pre
            temp.prev = self.lru[key]

