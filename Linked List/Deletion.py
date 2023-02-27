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
        
    def deletion_beg(self):
        temp = self.head.next
        self.head = temp
        
    
    def deletion_end(self):
        temp = self.head
        while(temp.next):
            last_node = temp
            temp = temp.next
        last_node.next = None
        
    def deletion_after(self, position):
        temp = self.head
        for i in range(0,position-1):
            last_node = temp
            temp = temp.next
        last_node.next = last_node.next.next
            
        

#creating object
llist = LinkedList()

#initializing head
llist.head = Node(1)

#creating nodes
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)
sixth = Node(6)

#linking to form a ll
llist.head.next = second 
second.next = third  
third.next = fourth
fourth.next = fifth
fifth.next = sixth

print("linked list: ")
llist.printList()


#DELETION AT BEGGINING
llist.deletion_beg()
llist.printList()

#DELETION AT END
llist.deletion_end()
llist.printList()

#DELETION AFTER NUMBER
llist.deletion_after(2)
llist.printList()



















