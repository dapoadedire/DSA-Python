class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedist:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node7 = cur_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

llist = Linkedist()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
# llist.print_list()


# llist.insert_after_node(llist.head, 'E')
llist.insert_after_node(llist.head.next, 'F')  
llist.print_list()