class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    """
    LRU Cache supporting O(1) get and put.
    Uses a combination of:
      1. A hash map (self.cache) mapping keys to nodes
      2. A doubly-linked list to maintain usage order:
         - The left (self.left) is the 'least recently used' (LRU) sentinel.
         - The right (self.right) is the 'most recently used' (MRU) sentinel.

    Time Complexity:
      - get(key) -> O(1)
      - put(key, value) -> O(1)
    Space Complexity:
      - O(capacity) for storing up to 'capacity' nodes in the cache.
    """

    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with given capacity.
        """
        self.cap = capacity                # The maximum number of items allowed
        self.cache = {}                    # Maps key -> Node for O(1) access

        # Create sentinel nodes for left (LRU end) and right (MRU end)
        self.left = Node(0, 0)            # LRU sentinel
        self.right = Node(0, 0)           # MRU sentinel

        # Link the two sentinels together
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: Node) -> None:
        """
        Remove a node from the doubly linked list.
        """
        prev, nxt = node.prev, node.next  # Get the node's neighbors
        prev.next = nxt                   # 'Skip' the node by linking neighbors
        nxt.prev = prev

    def insert(self, node: Node) -> None:
        """
        Insert a node right before the MRU sentinel (self.right).
        This position is considered the 'most recently used' position.
        """
        prev, nxt = self.right.prev, self.right  # The node currently at the MRU end
        prev.next = nxt.prev = node              # Link both neighbors to 'node'
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        """
        Return the value of the key if it exists in the cache.
        If it exists, move the node to the MRU position (right end).
        If the key is not present, return -1.
        """
        if key in self.cache:
            # Move the accessed node to MRU position
            self.remove(self.cache[key])   # Remove from its current position
            self.insert(self.cache[key])   # Re-insert at MRU
            return self.cache[key].val
        return -1                          # Key not found

    def put(self, key: int, value: int) -> None:
        """
        Update or insert the value if key exists. Otherwise, add a new entry.
        If adding a new entry exceeds capacity, remove the LRU entry.
        """
        if key in self.cache:
            # Key already exists: remove the old node before reinserting
            self.remove(self.cache[key])

        # Create/Update the node in the cache
        self.cache[key] = Node(key, value)

        # Insert the new or updated node at the MRU position
        self.insert(self.cache[key])

        # Check if capacity exceeded
        if len(self.cache) > self.cap:
            # Identify the LRU node at self.left.next
            lru = self.left.next
            self.remove(lru)              # Remove it from the DLL
            del self.cache[lru.key]       # Remove it from the hashmap

lru = LRUCache(3)
lru.put(1, 1)
lru.put(3, 3)
lru.put(2, 2)
lru.put(5, 2)
print(lru.get(2))

