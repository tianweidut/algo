class LRUCache:
    class DoubleLinkedNode:
        def __init__(self, key=-1, val=-1):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None

        def __str__(self) -> str:
            return f"{self.key}:{self.val}"

    def __init__(self, capacity: int):
        assert capacity > 0, "capacity must be greater than zero"
        self.capacity = capacity

        self.head = self.DoubleLinkedNode()
        self.tail = self.DoubleLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.key_map = {}

    def get(self, key: int) -> int:
        if key in self.key_map:
            self.move_to_tail(self.key_map[key])
            return self.key_map[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_map:
            self.move_to_tail(self.key_map[key])
            self.key_map[key].val = value
        else:
            if self.capacity == len(self.key_map):
                node = self.head.next
                self.remove_node(node)
                del self.key_map[node.key]

            node = self.DoubleLinkedNode(key=key, val=value)
            self.insert_to_tail(node)
            self.key_map[key] = node

    def move_to_tail(self, node):
        if not node:
            return
        self.remove_node(node)
        self.insert_to_tail(node)

    def remove_node(self, node):
        if not node:
            return

        node.next.prev = node.prev
        node.prev.next = node.next

        node.prev = None
        node.next = None

    def insert_to_tail(self, node):
        if not node:
            return

        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev = node
        node.prev.next = node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
