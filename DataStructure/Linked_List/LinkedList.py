class Node:

    def __init__(self,data):
        self.head = data
        self.next = None



class LinkedList:

    def __init__(self):
        self.head = None

    def insertAtBegin(self,data):
        new_node = Node(data)
        if new_node is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def printLL(self):
        currentNode = self.head
        while(currentNode):
            print(currentNode.data)
            currentNode = currentNode.next

    
llist = LinkedList()
llist.insertAtBegin(5)
llist.insertAtBegin(6)
llist.insertAtBegin(7)
llist.insertAtBegin(8)

print("Print Linked List")
llist.printLL()

