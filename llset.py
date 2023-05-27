class LLSet:
    class Node:
        def __init__(self, val, next):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None

    def insert(self, item):
        if self.contains(item):
            return False
        
        trav = self.head
        if trav is None:
            self.head = self.Node(item, None)
            return True
        
        while trav.next is not None:
            trav = trav.next
        
        trav.next = self.Node(item, None)
        return True

    def contains(self, item):
        trav = self.head
        return self.__contains(trav, item)
    
    def __contains(self, node, item):
        if not node:
            return False
        
        if node.val == item:
            return True
        
        return self.__contains(node.next, item)

    def delete(self, item):
        if not self.contains(item):
            return False
        
        trav = self.head
        prev = None
        while trav is not None:
            if trav.val == item:
                if prev is None:
                    self.head = trav.next
                else:
                    prev.next = trav.next
                return True
            
            prev = trav
            trav = trav.next
        
        return False

    def size(self):
        trav = self.head
        return self.__size(trav)
    
    def __size(self, node):
        if not node:
            return 0
        return 1 + self.__size(node.next)

    def to_list(self):
        new_list = []
        trav = self.head

        while trav is not None:
            new_list.append(trav.val)
            trav = trav.next
        
        return new_list
