

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        node = self.head
        while node.next:
            node = node.next
        
        node.next = new_node
        self.tail = new_node

    def delete(self, value):

        if not self.head:
            return

        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return

        node = self.head
        while node.next:
            if node.next.value == value:
                if node.next == self.tail:
                    self.tail = node
                node.next = node.next.next
                return
            node = node.next


    
    
        

    def printLL(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next


ss = SinglyLinkedList()
ss.append(1)
ss.append(2)
ss.append(5)
ss.delete(5)
ss.printLL()
