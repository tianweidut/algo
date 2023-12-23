class DoubleLinkNode:
	def __init__(self, val=0, n=None, p=None):
		self.val = val
		self.next = n
		self.prev = p

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}

        self.head = DoubleLinkNode()
        self.tail = DoubleLinkNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.map:
            val, node = self.map[key]
            self.use(node)
            return val
        else:
            return -1

    def put(self, key: int, val: int) -> None:
        if key not in self.map:
            node = DoubleLinkNode(key)
        else:
            _, node = self.map[key]

        self.use(node)
        self.map[key] = val, node

        if len(self.map) > self.capacity:
            self.pop()


    def use(self, node):
        if not node:
            return

        # for the existed node
        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev

        # head next
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def pop(self):
        if self.tail.next is self.head:
            return

        del self.map[self.tail.prev.val]

        pparent = self.tail.prev.prev
        pparent.next = self.tail
        self.tail.prev = pparent





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
