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
        
    def insertion_beg(self, data):
        temp = Node(data)
        temp.next = llist.head
        llist.head = temp
    
    def insertion_end(self, data):
        new_node = Node(data)
        temp = self.head

        while (temp):
            if (temp.next == None):
                temp2 = temp 
            temp = temp.next
                
        temp2.next = new_node
        
    def insertion_after(self, number, value):
        new_node = Node(value)
        temp = self.head
        
        while (temp):
            if (temp.data == number):
                temp1 = temp.next
                temp.next = new_node
                new_node.next = temp1
                return 0
            temp = temp.next
            

  
#creating object
llist = LinkedList()

#initializing head
llist.head = Node(1)

#creating nodes
second = Node(2)
third = Node(3)

#linking to form a ll
llist.head.next = second 
second.next = third  

print("linked list: ")
llist.printList()


#INSERTION AT BEGGINING
llist.insertion_beg(4)
print("\nInsertion at beggining: " )
llist.printList()


#INSERTION AT END
llist.insertion_end(5)
print("\nInsertion at end: ")
llist.printList()


#INSERTION AT SPECIFIC POSITION
number = 2 #number after which insertion has to be pernformed
new_data3 = 6
llist.insertion_after(number, new_data3)
print("\nInsertion after a number: ")
llist.printList()


















