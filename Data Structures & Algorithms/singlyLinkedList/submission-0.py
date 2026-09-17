class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        if self.head is None:
            return -1
        else:
            curr = self.head
            idx = 0
            while curr is not None and idx != index:
                curr = curr.next
                idx += 1
            
            if curr is not None and idx == index:
                return curr.val
            else:
                return -1

    def insertHead(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val, None)
        else:
            new_head = Node(val, None)
            new_head.next = self.head
            self.head = new_head

    def insertTail(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val, None)
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(val, None)

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        else:
            curr = self.head.next
            prev = self.head
            idx = 1
            while curr is not None and idx != index:
                curr = curr.next
                prev = prev.next
                idx += 1
            
            if curr is not None and idx == index:
                prev.next = curr.next
                return True
            else:
                return False

    def getValues(self) -> List[int]:
        curr = self.head
        res = []
        while curr is not None:
            res.append(curr.val)
            curr = curr.next
        return res
