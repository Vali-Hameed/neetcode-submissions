class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    def __init__(self):
        # The sentinel node simplifies edge cases for insertion/deletion.
        # It always exists at the beginning and doesn't hold actual data.
        self.head = Node(-1) 
        self.tail = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        current = self.head.next # Skip the sentinel node
        for _ in range(index):
            current = current.next
        return current.val

    def insertHead(self, val: int) -> None:
        new_node = Node(val, self.head.next)
        self.head.next = new_node
        if self.size == 0: # If list was empty, new node is also the tail
            self.tail = new_node
        self.size += 1

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        self.tail.next = new_node # Link the old tail to the new node
        self.tail = new_node      # Update the tail pointer
        self.size += 1
    
    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False
            
        # Find the node *before* the one to remove
        current = self.head 
        for _ in range(index):
            current = current.next
            
        # If removing the tail, update the tail pointer
        if current.next == self.tail:
            self.tail = current

        # Bypass the node to be removed
        current.next = current.next.next
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        values = []
        current = self.head.next # Start from the first actual node
        while current:
            values.append(current.val)
            current = current.next
        return values