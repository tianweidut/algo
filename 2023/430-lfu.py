class DoubleLinkedNode:
    def __init__(self, key=-1, val=-1) -> None:
        self.key = key
        self.val = val
        self.freq = 1
        self.next = None
        self.prev = None


class FreqDoubleLinkedList:
    def __init__(self) -> None:
        self.head = DoubleLinkedNode()
        self.tail = DoubleLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cnt = 0


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity

        self.freq_map = {}
        self.key_map = {}

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1

        node = self.key_map[key]
        self.pop_up_node(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key_map:
            node = self.key_map[key]
            node.val = value
            self.pop_up_node(node)
        else:
            if len(self.key_map) == self.capacity:
                min_freq = min(self.freq_map)
                node = self.freq_map[min_freq].head.next
                del self.key_map[node.key]
                self.remove_node(node)

            node = DoubleLinkedNode(key=key, val=value)
            self.key_map[key] = node
            self.insert_to_tail(node)

    def pop_up_node(self, node):
        self.remove_node(node)

        node.freq += 1
        self.insert_to_tail(node)

    def remove_node(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

        # do not change freq value
        node.next = None
        node.prev = None

        # cleanup linked list
        linked_list = self.freq_map[node.freq]
        linked_list.cnt -= 1

        if linked_list.cnt == 0:
            del self.freq_map[node.freq]

    def insert_to_tail(self, node):
        if node.freq not in self.freq_map:
            self.freq_map[node.freq] = FreqDoubleLinkedList()

        linked_list = self.freq_map[node.freq]
        linked_list.cnt += 1
        node.prev = linked_list.tail.prev
        node.next = linked_list.tail
        node.prev.next = node
        node.next.prev = node

obj = LFUCache(2)
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
obj.put(3, 3)
print(obj.get(2))
print(obj.get(3))
obj.put(4, 4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))
