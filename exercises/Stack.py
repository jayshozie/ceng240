# MIT License
# Copyright (c) 2025 Emir Baha Yıldırım
# Please see the LICENSE file for more details.

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        print(item, "pushed.")
        return item

    def pop(self):
        if not self.isEmpty():
            tmp = self.items[-1]
            self.items.pop()
            print(tmp, "popped.")
            del tmp
        else:
            return "Empty stack, can't pop."
        
    def size(self):
        print("Size:", len(self.items))
        return len(self.items)
    
    def peek(self):
        if not self.isEmpty():
            print("Top:", self.items[-1])
            return self.items[-1]
        else:
            return "Empty stack."
        
    def show(self):
        if not self.isEmpty():
            showList = []
            for i in self.items:
                showList.append(i)
            print("Bottom |", showList, "| Top")
            return showList
        else:
            return "Empty stack."

"""

stack = Stack()
for i in range(10):
    stack.push(i+5)
stack.size()
stack.peek()
stack.pop()
stack.size()
stack.peek()
stack.show()

"""

"""

stack = Stack()
for i in range(10):
    stack.push(i+4)
stack.show()
stack.pop()
stack.peek()
stack.show()

"""
