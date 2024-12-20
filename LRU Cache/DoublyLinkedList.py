class DLNode:
    def __init__(self, key, value):
        # Initialize a new node in a doubly linked list.
        # Each node stores a key-value pair.
        
        self.key = key  # The key associated with the node (can be used for identification).
        self.value = value  # The value/data stored in the node.
        
        self.prev = None  # A reference to the previous node in the list (initially None).
        self.next = None  # A reference to the next node in the list (initially None).
