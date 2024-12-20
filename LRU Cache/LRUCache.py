from DoublyLinkedList import DLNode

# Class definition of Least Recently Used Cache.
class LRUCache:
    # initiator.
    def __init__(self, capacity: int):
        # Ensure the capacity is greater than 0 and cannot exceed 50
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")
        
        self._capacity = min(capacity, 50)  # Set capacity to 50 if it exceeds 50
        self._cache = {}  # A dictionary to store the cache items for quick access by key.

        # Create dummy head and tail nodes for the doubly linked list.
        # These nodes will not hold actual data, but help in managing the list boundaries.
        self._head = DLNode(0, 0)  # Dummy head node, initialized with a key and value of 0.
        self._tail = DLNode(0, 0)  # Dummy tail node, initialized with a key and value of 0.

        # Set up the initial connections between head and tail.
        # Initially, the list is empty, so head is connected directly to tail.
        self._head.next = self._tail  # Head's next points to the tail.
        self._tail.prev = self._head  # Tail's previous points to the head.

        self._accesses = 0
        self._misses = 0

#-------------------------------------------------------------------------------------------------------------------------

    # Function to remove the node from the doubly linked list.
    def _remove(self, node):
        # This method removes a node from the doubly linked list.
        # It does not delete the node itself, just updates the connections to skip over it.

        previous = node.prev  # Get the node before the one to be removed.
        previous.next = node.next  # Point the 'next' of the previous node to the node after the current one.
            
        node.next.prev = previous  # Update the 'prev' pointer of the next node to skip over the current node.

#-------------------------------------------------------------------------------------------------------------------------

    # Function to add a node right after the head (most recently used position).
    def _add(self, node):
        # This method adds a node right after the head of the doubly linked list.
        # The head node represents the least recently used boundary, and new nodes are added after it.

        node.next = self._head.next  # Set the 'next' pointer of the new node to the current first node.
        node.prev = self._head  # Set the 'prev' pointer of the new node to the head.

        self._head.next = node  # Update the 'next' pointer of the head to point to the new node.
        node.next.prev = node  # Update the 'prev' pointer of the former first node to point to the new node.

#-------------------------------------------------------------------------------------------------------------------------

    # Get method to retrieve a value by key.
    def get(self, key: int) -> int:
        # Check if the key exists in the cache.
        self._accesses += 1

        if key in self._cache:
            node = self._cache[key]  # Retrieve the node associated with the key.

            # Since the node has been accessed, it is now the most recently used.
            # We need to remove it from its current position and add it back to the front.
            self._remove(node)  # Remove the node from its current position in the list.
            self._add(node)  # Add the node back to the front (just after the head).

            return node.value  # Return the value associated with the key.

        self._misses += 1
        return -1  # Return -1 if the key is not in the cache.
    
#-------------------------------------------------------------------------------------------------------------------------

    def put(self, key: int, value: int) -> None:
        self._accesses += 1

        # Ensure the key and value are within valid ranges
        if key < 0 or key >= 100:
            raise ValueError("Key must be greater than or equal to 0 and less than 100.")
        if value < 0 or value >= 100:
            raise ValueError("Value must be greater than or equal to 0 and less than 100.")

        # If the key already exists in the cache
        if key in self._cache:
            node = self._cache[key]
            node.value = value  # Update the value of the existing node
            self._remove(node)  # Move the node to the most recently used position
            self._add(node)
        else:
            # Handle a new key
            self._misses += 1  # Count a miss for the new key
            if len(self._cache) >= self._capacity:  # If at capacity, evict the least recently used (LRU) item
                lru = self._tail.prev
                self._remove(lru)
                del self._cache[lru.key]
            # Add the new key-value pair to the cache
            node = DLNode(key, value)
            self._add(node)
            self._cache[key] = node

#------------------------------------------------------------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        # Resize the cache to a new capacity, ensuring it doesn't exceed 50 and is greater than 0.
        if new_capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")
        
        self._capacity = min(new_capacity, 50)  # Set capacity to 50 if it exceeds 50
        
        # Evict items if the cache is over capacity after resizing.
        while len(self._cache) > self._capacity:
            lru = self._tail.prev  # The least recently used (LRU) node is just before the tail.
            self._remove(lru)  # Remove the LRU node from the doubly linked list.
            del self._cache[lru.key]  # Remove the LRU node's key from the cache dictionary.

#------------------------------------------------------------------------------------------------------------------------

    def miss_rate(self):
        # Check if there have been any accesses to avoid division by zero
        if self._accesses == 0:
            return 0.0  # No accesses imply a miss rate of 0
        miss_rate = self._misses / self._accesses
        return miss_rate
    
#=========================================================================================================================
