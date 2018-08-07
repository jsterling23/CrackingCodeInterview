

# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = Node()

#     def append(self, data):
#         new_node = Node(data)
#         current = self.head
#         while current.next != None:
#             current = current.next
#         current.next = new_node

#     def display(self):
#         elems = []
#         current_node = self.head
#         while current_node.next != None:
#             current_node = current_node.next
#             elems.append(current_node.data)
#         print(elems)
#         return elems

#     def removeDuplicate(self):
#         hashTable = {}
#         current_node = self.head
#         while current_node.next != None:
#             prev_node = current_node
#             current_node = current_node.next
#             if current_node.data in hashTable:
#                 prev_node.next = current_node.next 
#             else:
#                 hashTable[current_node.data] = True
#         print(hashTable)



class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    
class LinkedList:
    def __init__(self):
        self.head = Node()


    def addToList(self, data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node

    def display(self):
        elems = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elems.append(current_node.data)
        print(elems)
        return elems

    def length(self):
        length = 0;
        current_node = self.head
        while current_node.next != None:
            length += 1
            current_node = current_node.next
        # print(length)
        return length

    def erase(self, index):
        current_index = 0;
        current_node = self.head
        while current_node.next != None:
            prev_node = current_node
            current_node = current_node.next
            if current_index == index:
                prev_node.next = current_node.next
            current_index += 1

    def removeDups(self):
        current_node = self.head
        hashTable = {}
        while current_node.next != None:
            prev_node = current_node
            current_node = current_node.next
            if current_node.data in hashTable:
                prev_node.next = current_node.next
            else:
                hashTable[current_node.data] = True;
        return self

    def get(self, index):
        current_node = self.head
        current_index = 0
        while current_node.next != None:
            current_node = current_node.next
            if current_index == index:
                print(current_node.data)
            current_index += 1
        
    def divideList(self, Linkedlist):
        if self.length() == 0:
            print("ERROR: List is empty")
            return None

        current_node = self.head
        node_runner = self.head

        while node_runner.next != None:
            node_runner = node_runner.next

            if node_runner.next == None:
                break

            node_runner = node_runner.next
            current_node = current_node.next

        toReturn = current_node.next
        current_node.next = None
        return toReturn
        



test = LinkedList();
test.addToList(4);
test.addToList(1);
test.addToList(2);
test.addToList(2);
test.addToList(3);
test.addToList(4);
test.addToList(2);
test.display();
test.divideList(test)
test.display();




































# my_list = LinkedList()

# my_list.append(2)
# my_list.append(16)
# my_list.append(4)
# my_list.append(2)
# my_list.append(6)
# my_list.append(2)
# my_list.append(27)
# my_list.append(29)
# my_list.append(16)
# my_list.append(22)
# my_list.append(2)
# my_list.append(77)
# my_list.append(2)
# my_list.append(27)
# my_list.append(29)
# my_list.append(16)
# my_list.append(22)

# my_list.display()

# my_list.removeDuplicate()
# my_list.removeDuplicate()
# my_list.removeDuplicate()
# my_list.display()






