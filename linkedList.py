class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data) -> None:
        self.data = data

    def __repr__(self) -> str:
        return f"Node(data={self.data})"

class LinkedList:
    """
    Singly linked list
    """
    def __init__(self) -> None:
        self.head: Node = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Returns the number of nodes in the list
        Runs in O(n) - linear time
        """
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.next_node
        
        return count

    def add(self, value):
        """
        Adds a new  Node containing data at head of the list
        Runs in O(1) time
        """
        new_node = Node(value)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, data):
        """
        Search for the first Node containing data that matches the data
        Return the node or `None` if not found

        Runs in O(n) time
        """ 
        current = self.head

        while current != None:
            if current.data == data:
                return current
            else:
                current = current.next_node
            
        return None
    
    def insert(self, value, index):
        """
        Inserts a new Node containing data at index position `index`
        Insertion takes O(1) time but finding the Node at the insertion point takes O(n) time
        Therefore, this method runs in O(n) time
        """
        if index == 0:
            self.add(value)
        
        if index > 0:
            new = Node(value)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1
            
            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, value):
        """
        Removes Node containing data that matches the key
        Returns the node or None if the key doesn't exist
        Runs in O(n) time
        """
        current = self.head
        previous: Node = None
        found =  False

        while current and not found:
            if current.data == value and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == value:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current

    def removeAt(self, index):
        """
        Removes Node at index position `index`
        Removal takes O(1) time but finding the Node at the removal point takes O(n) time
        Therefore, this method runs in O(n) time
        """
        current: Node = self.head
        if index == 0:
            self.head = current.next_node
        
        if index > 0:
            position = index

            while position > 1:
                current = current.next_node
                print(current)
                position -= 1

            previous = current
            current = current.next_node
            previous.next_node = current.next_node

        return current

    def getAtIndex(self, index):
        """
        Returns the value at an index
        Runs in O(n) time
        """
        current = self.head
        
        while current and index > 0:
            current = current.next_node
            index -= 1
        
        return current

    def __repr__(self) -> str:
        """
        Return a string representaion of the list
        Runs in O(n) time
        """

        nodes = []
        current = self.head

        while current != None:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"[{current.data}]")
            
            current = current.next_node
        
        return '-> '.join(nodes)

lst = LinkedList()

from random import randint

for i in range(10):
    lst.add(randint(1, 10000))