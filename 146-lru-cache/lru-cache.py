class DListNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Maps key to DListNode
        # Create dummy head and tail for easy manipulation
        self.head = DListNode()  
        self.tail = DListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: DListNode):
        """ Remove node from the doubly linked list. """
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_at_front(self, node: DListNode):
        """ Insert node at the front of the list (just after the head). """
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Move the accessed node to the front (most recent)
            self._remove(node)
            self._insert_at_front(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove the old node if it exists
            node = self.cache[key]
            self._remove(node)
        else:
            node = DListNode(key, value)
            self.cache[key] = node
        
        # Insert the node at the front (most recent)
        node.value = value
        self._insert_at_front(node)

        # If the cache exceeds the capacity, remove the least recently used node
        if len(self.cache) > self.capacity:
            # Remove the node from the tail (LRU)
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)