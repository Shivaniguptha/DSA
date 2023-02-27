class Node:
    
    #node creation
    def __init__(self, data):
        self.data = data  
        self.next = None 
  
class LinkedList:
    
    #linked list initialization
    def __init__(self):
        self.head = None
        
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, "-> ", end = "")
            temp = temp.next
        print("NULL")
        
    def push(self, data):
        new_node = Node(data)
        temp = self.head
        temp2 = self.head
        
        if (temp2 == None):
            self.head = new_node
            
        while (temp):
            if (temp.next == None):
                temp.next = new_node
                return 0
            temp = temp.next
                
        
            
        
llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.printList()
