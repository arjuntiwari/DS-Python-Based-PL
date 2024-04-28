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
    
    def insertAtEnd(self,data):
        new_node = Node(data)
        node_head = self.head
        if node_head is None:
            self.head = new_node
            return
        else:
            while(node_head.next != None):
                node_head = node_head.next
            
            node_head.next = new_node
    
    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if(position == index):
            self.insertAtBegin(data)
            return
        else:
            while(current_node != None and position + 1 != index):
                position = position + 1
                current_node = current_node.next
            
            if current_node != None:
               new_node.next = current_node.next
               current_node.next = new_node
            else:
                print('index not present')
    
    def updateNode(self,data,index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if(position == index and current_node != None):
            current_node.head = new_node
        else:
            while(current_node != None and position + 1 != index):
                position = position + 1
                current_node = current_node.next
            
            if(current_node != None):
                current_node.head = data
            else:
                print('index not present')

    def removeFirstNode(self):
        if self.head == None :
            return
        
        self.head = self.head.next

    def removeLastNode(self):
        if self.head is None:
            return
 
        current_node = self.head
        while(current_node.next.next):
            current_node = current_node.next
 
        current_node.next = None

        
    def removeAtIndex(self,index):
        if self.head == None:
            return
        
        current_node = self.head
        position = 0
        if position == index:
            self.removeFirstNode()
        else:
            while(current_node != None and position + 1 != index):
                position = position + 1
                current_node = current_node.next
        
        if current_node != None:
            current_node.next = current_node.next.next
        else:
            print('index not present')
    
    def listSize(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size + 1
                current_node = current_node.next
            
            return print(size)

        else:
            return print(0)


    def printLL(self):
        currentNode = self.head
        while(currentNode):
            print(currentNode.head)
            currentNode = currentNode.next

    

    
llist = LinkedList()
llist.insertAtBegin(5)
llist.insertAtBegin(2)
llist.insertAtBegin(2)
llist.insertAtBegin(8)
llist.insertAtEnd(3)
llist.insertAtEnd(0)
llist.insertAtIndex(11,2)

print("Print Linked List")
llist.printLL()

print("update node 4")
llist.updateNode(12,4)
llist.printLL()

print("remove first node")
llist.removeFirstNode()
llist.printLL()

print("remove last node")
llist.removeLastNode()
llist.printLL()

print("remove at index")
llist.removeAtIndex(4)
llist.printLL()

print("size of list")
llist.listSize()


