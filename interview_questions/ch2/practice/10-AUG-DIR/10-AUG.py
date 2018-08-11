
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
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def display(self):
        elems = []
        last_node = self.head
        while last_node:
            elems.append(last_node.data)
            last_node = last_node.next
        print(elems)
        return elems
    
    def length(self):
        length = 0
        runner = self.head
        while runner:
            length += 1
            runner = runner.next
        print(length)
        return length


    def get(self, target):
        runner = self.head
        curr_idx = 0
        while runner:
            if curr_idx == target:
                print(runner.data)
                return runner.data
            else:
                curr_idx += 1
                runner = runner.next


    def insert_after_node(self, prev_node, data):

        if not prev_node:
            print('This node does not exist')
            return
        
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node



    def deleteNode(self, key):
        curr_node = self.head
        
        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return
 
        while curr_node and curr_node.data != key:
            prev_node = curr_node
            curr_node = curr_node.next

        if curr_node is None:
            print('Data not in the list')
            return

        prev_node.next = curr_node.next
        curr_node = None



    def delete_at_position(self, position):
        curr_node = self.head
        curr_idx = 1

        if curr_node and curr_idx == position:
            self.head = curr_node.next
            curr_node = None
            return
        
        prev_node = None
        while curr_node and curr_idx != position:
            prev_node = curr_node
            curr_node = curr_node.next
            curr_idx += 1

        if curr_node is None:
            print('Dude.. that postion does NOT exist')
            return
        prev_node.next = curr_node.next
        curr_node = None

    def deleteDuplicates(self):
        curr_node = self.head
        prev_node = None
        hashTable = {}

        while curr_node:
            if curr_node.data in hashTable:
                prev_node.next = curr_node.next
                curr_node = None #this is why line 126 can't be curr_node = current_node.next
            else:
                hashTable[curr_node.data] = True
                prev_node = curr_node
            curr_node = prev_node.next 

    def deleteMiddleNode(self):
        target = round(self.length() / 2)
        curr_idx = 0
        curr_node = self.head
        prev_node = None

        while curr_node:
            if target == curr_idx:
                prev_node.next = curr_node.next
                return
            else:
                prev_node = curr_node
                curr_idx += 1
            curr_node = prev_node.next

    def retrieve_last_node(self):
        curr_node = self.head
        while curr_node:
            if curr_node.next == None:
                print(curr_node.data)
                return curr_node.data
            else:
                curr_node = curr_node.next

    def split_list(self):
        current_node = self.head
        runner = self.head

        while runner:
            if runner.next != None:
                runner = runner.next
            else:
                break
            runner = runner.next
            current_node = current_node.next
        returnList = current_node.next
        current_node.next = None
        return returnList

    def sum_list(self, list2):
        list1 = self.head
        list2 = list2.head
        new_list = LinkedList()
        carry = 0

        while list1 and list2:
            if list1:
                i = list1.data
            else:
                i = 0
            if list2:
                j = list2.data
            else:
                j = 0
            s = i + j + carry
            if s >= 10:
                carry = 1
                remainder = s % 10
                new_list.prepend(remainder)
            else:
                carry = 0
                new_list.prepend(s)
            list1 = list1.next
            list2 = list2.next
        if carry > 0:
            new_list.prepend(carry)
        
        new_list.display()


    def hacky_way_to_reverse(self, list1):
        curr_node = list1.head #Assuming this list is forward
        new_list = LinkedList() #prepending here then returning

        while curr_node:
            new_list.prepend(curr_node.data)
            curr_node = curr_node.next
        new_list.display()
        return new_list


    def reverse_list(self):

        current_node = self.head
        prev = None

        while current_node:
            nxt = current_node.next
            current_node.next = prev

            prev = current_node
            current_node = nxt
        self.head = prev



llist1 = LinkedList()
llist2 = LinkedList()
alphaList = LinkedList()

alphaList.append("A")
alphaList.append("B")
alphaList.append("C")
alphaList.append("D")
alphaList.append("E")
alphaList.append("F")
alphaList.append("G")
alphaList.append("H")
alphaList.append("I")
alphaList.display()


# llist1.display()
# llist1.insert_after_node(1,)
# llist1.insert_after_node(llist1.head.next,'E')
# llist1.get(2)
# llist1.length()
# llist1.deleteNode("C")
# llist1.delete_at_position(4)
# llist1.deleteDuplicates()
# llist1.deleteMiddleNode()
# llist1.retrieve_last_node()
# llist1.split_list()
# llist1.display()


# llist2.prepend('A')
# llist2.prepend('B')
# llist2.prepend('C')
# llist2.display()
# llist2.length()


llist1.append(1)
llist1.append(1)
llist1.append(1)
llist1.append(5)
# llist1.display()

llist2.append(1)
llist2.append(1)
llist2.append(1)
llist2.append(5)
# llist2.display()

# llist1.sum_list(llist2)
# llist1.hacky_way_to_reverse(llist1)

# alphaList.hacky_way_to_reverse(alphaList)
alphaList.reverse_list()
alphaList.display()

