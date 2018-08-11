

class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = node()

    def addToList(self, data):
        new_node = node(data)
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
        print('Linked List >> ',elems)
        return elems

    def SumTwoLists(self, list2):
        list1 = self.head
        list2 = list2.head
        sum_list = LinkedList()
        carry = 0
        count = 0

        list1 = list1.next
        list2 = list2.next
        
        while list1 or list2:
            print('carry: ', carry)
            if not list1:
                i = 0
            else:
                i = list1.data

            if not list2:
                j = 0
            else:
                j = list2.data
            
            s = i + j + carry

            if s >= 10:
                carry = 1
                remainder = s % 10
                sum_list.addToList(remainder)
            else:
                carry = 0
                sum_list.addToList(s)
            
            list1 = list1.next
            list2 = list2.next

        sum_list.display()




list1 = LinkedList()
list1.addToList(3)
list1.addToList(4)
list1.addToList(3)
list1.display()


list2 = LinkedList()
list2.addToList(5)
list2.addToList(8)
list2.addToList(2)
list2.display()

list1.SumTwoLists(list2)

