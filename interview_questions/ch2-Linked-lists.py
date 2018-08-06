

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def display(self):
        elems = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elems.append(current_node.data)
        print(elems)
        return elems

    def removeDuplicate(self):
        hashTable = {}
        current_node = self.head
        while current_node.next != None:
            prev_node = current_node
            current_node = current_node.next
            if current_node.data in hashTable:
                prev_node.next = current_node.next 
            else:
                hashTable[current_node.data] = True
        print(hashTable)






my_list = LinkedList()

my_list.append(2)
my_list.append(16)
my_list.append(4)
my_list.append(2)
my_list.append(6)
my_list.append(2)
my_list.append(27)
my_list.append(29)
my_list.append(16)
my_list.append(22)
my_list.append(2)
my_list.append(77)
my_list.append(2)
my_list.append(27)
my_list.append(29)
my_list.append(16)
my_list.append(22)

my_list.display()

my_list.removeDuplicate()
my_list.removeDuplicate()
my_list.removeDuplicate()
my_list.display()
