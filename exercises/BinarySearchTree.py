# MIT License
# Copyright (c) 2025 Emir Baha Yıldırım
# Please see the LICENSE file for more details.

class Node:
    """
    A class to represent a node in a binary search tree.

    Attributes
    ----------
    value : Any
        The value stored in the node.
    left : Node or None
        A reference to the left child node.
    right : Node or None
        A reference to the right child node.
    """
    def __init__(self, value):
        """
        Initializes a Node object with the given value and sets the left and right children to None.

        Parameters
        ----------
        value : Any
            The value to store in the node.
        """
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        """
        Returns a string representation of the node's value.

        Returns
        -------
        str
            The string representation of the node's value.
        """
        return str(self.value)

class BinarySearchTree:
    """
    A class to represent a Binary Search Tree (BST).

    This class provides functionality to create and manage a binary search tree,
    including inserting values and searching for specific values.

    Attributes
    ----------
    root : Node or None
        The root node of the binary search tree. Initially set to None.

    Methods
    -------
    __init__():
        Initializes the BinarySearchTree object with an empty root.
    insert(value):
        Inserts a value into the binary search tree.
    _insert_recursive(node, value):
        Recursively inserts a value into the binary search tree (helper method).
    search(value):
        Searches for a value in the binary search tree and returns the corresponding node if found.
    _search_recursive(node, value):
        Recursively searches for a value in the binary search tree (helper method).
    """
    def __init__(self):
        """
        Initializes the BinarySearchTree object with an empty root.

        Parameters
        ----------
        None
        """
        self.root = None

    def insert(self, value):
        """
        Inserts a value into the binary search tree.

        If the tree is empty, the value is set as the root node. Otherwise, the value
        is inserted into the appropriate position in the tree.

        Parameters
        ----------
        value : int or float
            The value to be inserted into the binary search tree.

        Returns
        -------
        None
        """
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        Recursively inserts a value into the binary search tree.

        This is a helper method used internally by the `insert` method.

        Parameters
        ----------
        node : Node
            The current node being evaluated during the recursive insertion.
        value : Any
            The value to be inserted into the binary search tree.

        Returns
        -------
        None
        """
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        """
        Searches for a value in the binary search tree.

        Parameters
        ----------
        value : Any 
            The value to search for in the binary search tree.

        Returns
        -------
        Node or None
            The node containing the value if found, or None if the value is not in the tree.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        Recursively searches for a value in the binary search tree.

        This is a helper method used internally by the `search` method.

        Parameters
        ----------
        node : Node
            The current node being evaluated during the recursive search.
        value : Any
            The value to search for in the binary search tree.

        Returns
        -------
        Node or None
            The node containing the value if found, or None if the value is not in the tree.
        """
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

"""
# Example usage
# Create an instance of BinarySearchTree
>> bst = BinarySearchTree()

# Insert values into the BST
>> bst.insert(5)
>> bst.insert(3)
>> bst.insert(7)
>> bst.insert(2)
>> bst.insert(4)
>> bst.insert(6)
>> bst.insert(8)

# Search for elements in the BST and print the results
>> print("Searching for elements:")
Searching for elements:
>> print(bst.search(4))  # Found, returns the node (4)
4
>> print(bst.search(9))  # Not found, returns None
None
"""
"""
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

search = eval(input("What are you searching for? "))
print("Searching for results...")
if bst.search(search) != None:
    print(bst.search(search))
else:
    print("Not found.")
"""
