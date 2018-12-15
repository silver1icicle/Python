"""
Introduction:
1. LL comprise of nodes
2. Each node consists of a value + a pointer to the next node.
3. The starting node of each LL is called as the header node.
4. LL are often compared with Array DS. However LL are more memory efficient and grow/ shrink at runtime. Also unlike an array,
   LL do not require contiguous memory space. 
5. However the lookup time for a specific element n the LL is Linear i.e. We have to begin searching for the specific element from the start till the end.
   Unlike Arrays, in which we have a direct/ constant lookup

6. LL in Python is implemented by creating a Node class and a LinkedList class.

7. Lets say we have to implement a LL to store following numbers (12, 79, 3, 100). Since we are inserting @ the start of the LL, the ultimate LL will be:
   100 -->  3 -->  79 -->  12 -->   NULL
   To ensure the same order as inserton, change code to insert numbers @ the end of the LL. But this will a Time Complexity of O(n) instead of O(1). 

NOTE:
* LL = Linked Lists
* DS = Data structure
"""

class Node(object):
    """ A class to define a node """
    def __init__(self, dataVal):
        """ Obj: Ctor of the class """
        self.data = dataVal
        self.next = None                   # The pointer is initially a NULL

    # Getters &  Setters
    def get_nextNode(self):
        """ Obj: Get the next node in the LL """
        return self.next
    
    def set_nextNode(self, nextNode):
        """ Obj: Set the next node in the LL """
        self.next = nextNode

    def get_data(self):
        """ Obj: To return the data value of the current node """
        return self.data
    

class LinkedList(object):
    """ A class to define a LL """
    def __init__(self, headNode = None):
        """ Ctor of the class """
        self.head = headNode

    def insert(self, data):
        """
            Obj: To insert a new node @ the start of the Linked List
                 Two other insert variants: 1) Insert @ the end
                                            2) Insett @ a specific position
            Time Complexity: O(1)...as it interacts only with the head pointer
        """
        newNode = Node(data)
        newNode.set_nextNode(self.head)
        self.head = newNode

    def size(self):
        """
            Obj: To determine the size of the LL
            Time Complexity: O(n)...as it visits each n every node in the list
        """
        count = 0
        currentPointer = self.head
        while(currentPointer):
            count += 1
            currentPointer = currentPointer.get_nextNode()
        return count

    def search(self, ele):
        """
            Obj: To search a specific element in the Linked List
            Time Complexity: O(n)...worst case scenario..assuming we didnt the element till we traveresed till the end
        """
        currentPointer = self.head
        flagFound = False
        while (currentPointer and flagFound is False):
            if currentPointer.get_data() == ele:
                flagFound = True
            else:
                currentPointer = currentPointer.get_nextNode()

        if flagFound is False and currentPointer is None:
            raise ValueError("Element not found in the LL")
        return currentPointer

    def delete(self, ele):
        """
            Obj: Delete is similar to search
            Time Complexity: O(n) in worst case
        """
        currentPointer = self.head
        previousPointer = None
        flagFound = False

        while(currentPointer and flagFound is False):
            if currentPointer.get_data() == ele:
                print("Data:--->", str(currentPointer.get_data()))
                flagFound = True
                if previousPointer is None:
                    self.head = currentPointer.get_nextNode()                     # Tricky
                else:
                    previousPointer.set_nextNode(currentPointer.get_nextNode())   # Reset the pointers
                
            else:
                previousPointer = currentPointer
                currentPointer = currentPointer.get_nextNode()

        if flagFound is False:
            raise ValueError("Element not found in List")

    def display(self):
        """ Obj: To display the elements of the Linked List"""
        currentPointer = self.head
        while(currentPointer):
            print(str(currentPointer.get_data()) + " --> "),
            currentPointer = currentPointer.get_nextNode()
        print("NULL")
                
            
        

if __name__ == '__main__':
    ll = LinkedList()  # Instantiate the LL class. The Header node gets created in its Ctor.
    ll.insert(12)      # Insert elements
    ll.insert(79)
    ll.insert(3)
    ll.insert(100)
    ll.display()       # Display the end result
    print "Total Elements in the LL:------>", ll.size()          

    ll.delete(12)
    ll.display()
    print "Total Elements in the LL:------>", ll.size()

    ll.delete(3)
    ll.display()
    print "Total Elements in the LL:------>", ll.size() 

    ll.delete(100)
    ll.display()
    print "Total Elements in the LL:------>", ll.size() 
        
    ll.delete(79)
    ll.display()
    print "Total Elements in the LL:------>", ll.size() 

        
