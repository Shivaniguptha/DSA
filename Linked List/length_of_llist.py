# Find Length of a Linked List 

class Node:
    
    #node creation
    def __init__(self, data):
        self.data = data  
        self.next = None 
  
class LinkedList:
    
    #linked list initialization
    def __init__(self):
        self.head = None
        
        
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
                
    def len(self, count):
        temp = self.head
        while(temp):
            count = count + 1
            temp = temp.next
        return count
            
        
llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)
llist.push(6)

count = 0
print(llist.len(count))














