# MIT License
# Copyright (c) 2025 Emir Baha Yıldırım
# Please see the LICENSE file for more details.

class Node:
    """
    A class to represent a node in a singly linked list.

    Attributes:
        data: The data stored in the node.
        next: A reference to the next node in the linked list.
    """
    def __init__(self, data):
        """
        Initializes a Node object with the given data and sets the next pointer to None.

        Args:
            data: The data to store in the node.
        """
        self.data = data
        self.next = None

class LinkedList:
    """
    A class to represent a singly linked list.

    Attributes:
        head: The head node of the linked list.
    """
    def __init__(self):
        """
        Initializes an empty linked list with the head set to None.
        """
        self.head = None

    def display(self):
        """
        Displays the elements of the linked list in order.

        Prints:
            The data of each node in the linked list, separated by spaces.
        """
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def insert(self, data):
        """
        Inserts a new node with the given data at the end of the linked list.

        Args:
            data: The data to store in the new node.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, data):
        """
        Deletes the first node with the given data from the linked list.

        Args:
            data: The data of the node to delete.

        Returns:
            None
        """
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current:
            prev.next = current.next

"""
# Example usage
# Create an instance of the LinkedList class
linked_list = LinkedList()

# Insert elements into the linked list
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)

# Display the initial linked list
print("Initial Linked List:")
linked_list.display()

# Insert a new node with data 5 into the linked list
linked_list.insert(5)
print("After inserting a new node (5):")
linked_list.display()

# Delete a node with data 2 from the linked list
linked_list.delete(2)
print("After deleting an existing node (2):")
linked_list.display() 
"""
"""
linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)
print("Initial Linked List:")
linked_list.display()
linked_list.delete(2)
print("After deleting an existing node (2):")
linked_list.display()
"""
