# Stack Data Structure

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
       if not self.isEmpty():
           return self.items[-1]
    def size(self):
        return len(self.items)

# myStack = Stack()
# myStack.push('A')
# myStack.push('B')
# myStack.push('C')
# myStack.push('D')
# myStack.push('E')
# print(myStack.peek())
# print(myStack.size())
# print(myStack.isEmpty())
# myStack.pop()
# print(myStack.peek())
# print(myStack.size())