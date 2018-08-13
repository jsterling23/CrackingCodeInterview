class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def display(self):
        elems = []
        current_node = self.head
        while current_node:
            elems.append(current_node.data)
            current_node = current_node.next
        print(elems)
        return elems



    def swap_nodes(self, key_1, key_2):
        list1 = self.head
        prev_list1 = None

        list2 = self.head
        prev_list2 = None

        while list1 and list1.data != key_1:
            prev_list1 = list1
            list1 = list1.next

        while list2 and list2.data != key_2:
            prev_list2 = list2
            list2 = list2.next

        if list1:
            prev_list1.next = list2
        else:
            self.head = list2

        if list2:
            prev_list2.next = list1
        else:
            self.head = list2

        temp = list1.next
        print('temp', temp)

        temp = list1.next
        list1.next = list2.next
        list2.next = temp

        print(list1.data)
        print(prev_list1.data)
        
        print(list2.data)
        print(prev_list2.data)

    def get_node_by_index(self, index):
        



list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
list1.display()
list1.swap_nodes(2, 4)
# list1.display()
# list1.reverse_linked_list_iteratave()
list1.display()
