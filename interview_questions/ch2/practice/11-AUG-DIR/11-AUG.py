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
    
    def prepend(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return
        
        current_node = self.head
        self.head = new_node
        new_node.next = current_node


    def display(self):
        current_node = self.head
        elems = []

        while current_node:
            elems.append(current_node.data)
            current_node = current_node.next
        print(elems)
        return elems

    def insert_after_specific_node(self, prev_node, data):

        if not prev_node:
            print('Node not in the database')
            return
        
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def length(self):
        length = 0
        current_node = self.head

        while current_node:
            length += 1
            current_node = current_node.next
        print('length of list: ', length)
        return length

    def get_by_value(self, value):
        current_node = self.head
        while current_node:
            if current_node.data == value:
                print('You retrieved data', current_node.data)
                return current_node.data
            else:
                current_node = current_node.next

    def get_by_index(self, target):
        if target < 0 or target >= self.length():
            print('Index not in range bro heim')
            return
        current_node = self.head
        index = 0

        while current_node:
            if index == target:
                print('Data at the index: ', current_node.data)
                return current_node.data
            else:
                index += 1
                current_node = current_node.next

    def delete_specific_node_by_index(self, index):
        if index < 0 or index >= self.length():
            print('Index not in range bro heim')
            return

        current_node = self.head
        curr_idx = 0
        prev_node = self.head

        if current_node and index == curr_idx:
            self.head = current_node.next
            current_node = None
            return

        while current_node:
            if index == curr_idx:
                print('Deleted llist index: ', curr_idx, ' With data: ', current_node.data)
                prev_node.next = current_node.next
                return
            prev_node = current_node
            current_node = prev_node.next
            curr_idx += 1

    def delete_specific_node_by_value(self, value):
        current_node = self.head

        if current_node and current_node.data == value:
            self.head = current_node.next
            current_node = None
            return

        prev_node = None

        while current_node and current_node.data != value:
            prev_node = current_node
            current_node = current_node.next
        
        if current_node is None:
            print('Node not in database...')
            return
        
        prev_node.next = current_node.next
        current_node = None

    def delete_node_at_specific_position(self, target):
        cur_node = self.head
        cur_pos = 1

        if cur_node and cur_pos == target:
            self.head = cur_node.next
            cur_node = None
            return
        prev_node = None

        while cur_node and cur_pos != target:
            prev_node = cur_node
            cur_node = cur_node.next
            cur_pos += 1
        
        if cur_node is None:
            print("That position doesn't exist...")
            return
        
        prev_node.next = cur_node.next
        cur_node = None

    def delete_duplicates(self):
        curr_node = self.head
        prev_node = None
        hashtable = {}

        while curr_node:
            if curr_node.data in hashtable:
                prev_node.next = curr_node.next
                curr_node = None
            else:
                hashtable[curr_node.data] = True
                prev_node = curr_node
            curr_node = prev_node.next

    def split_list(self):
        curr_node = self.head
        runner = self.head

        while runner:
            runner = runner.next
            if runner.next != None:
                runner = runner.next
            else:
                break
            curr_node = curr_node.next
        toReturn = curr_node
        curr_node.next = None
        return toReturn
    
    def find_last_node(self):
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
        print(curr_node.data)
        return curr_node.data

    def delete_node_at_middle(self):
        curr_node = self.head
        target = round(self.length() / 2)
        curr_index = 1
        prev_node = None

        while curr_node and curr_index != target:
            prev_node = curr_node
            curr_node = curr_node.next
            curr_index += 1

        prev_node.next = curr_node.next
        curr_node = None
            
    def sum_lists(self, list2):
        list1 = self.head
        list2 = list2.head
        new_list = LinkedList()
        carry = 0

        while list1 and list2:
            if list1:
                i = list1.data
                list1 = list1.next
            else:
                i = 0
            
            if list2:
                j = list2.data
                list2 = list2.next
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

        if carry > 0:
            new_list.prepend(carry)

        new_list.display()

    def print_helper(self, node, name):
        if node is None:
            print(name, ": None")
        else:
            print(name,':', node.data)

    def reverse_list(self):
        current_node = self.head
        prev_node = None

        # update each node to point to the last node while traversing the list
        while current_node:
            # store the next node
            # point current node(current_node.next) to whatever the Prev node is

            # store current node as the previous
            # store the next node as the current node
            # break the loop
        # assign the new head to be the last node in the list thus reversing it.

            next_node = current_node.next
            current_node.next = prev_node

            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def reverse_recursive(self):

        def reversing_function(current_node, prev_node):
            if not current_node:
                return prev_node
            next_node = current_node.next
            current_node.next = prev_node

            prev_node = current_node
            current_node = next_node
            return reversing_function(current_node, prev_node)
        
        self.head = reversing_function(current_node=self.head, prev_node=None)

    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            print("You are an idiot...")
            return

        prev_1 = None
        curr_1 = self.head
        # When this loop makes it's way through it needs the correct key to quit.
        # When it finds the correct key, it will then have the current node stored
        # along with the previous node pertaining to the 1st list
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next
        print('prev 1', prev_1.data)
        print('curr_1.next', curr_1.data)

        prev_2 = None
        curr_2 = self.head
        # This loop is the same as above in that it will stop when the conditons are
        # met. WHen it stops then I should have a prev_2 and curr_2 with their respective
        # values ready to use.
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next
        print('prev 2', prev_2.data)
        print('curr_2.next ', curr_2.data)
        
        # if it made it through both loops and neigther of the keys hit, then it should
        # execute this statement and return. Meaning that what was entered was gay.
        if not curr_1 or not curr_2:
            print('One of these dont exist')
            return
        

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        # curr_1.next, curr_2.next = curr_2.next, curr_1.next






    # def swap_nodes(self, key_1, key_2):




list1 = LinkedList()
list2 = LinkedList()

list1.append('A')
list1.append('B')
list1.append('C')
list1.append('Jeffrey')
# list1.display()

list2.append(1)
list2.append(2)
list2.append(3)
list2.append(4)
# list2.display()

# list1.sum_lists(list2)
# list2.reverse_list()
# list2.reverse_recursive()
list1.display()
list1.swap_nodes('B','Jeffrey')
list1.display()


# list1.append(1)
# list1.append(2)
# list1.append(4)
# list1.append(5)
# list1.append('Middle')
# list1.append(7)
# list1.append(8)
# list1.append(9)
# list1.append(10)
# list1.append(11)

# list1.insert_after_specific_node(list1.head.next,3)
# list1.prepend(7)
# list1.display()
# list1.delete_specific_node_by_index(0)
# list1.delete_specific_node_by_value('baby cakes')
# list1.delete_node_at_specific_position(1)
# list1.delete_duplicates()
# list1.split_list()
# list1.find_last_node()
# list1.delete_node_at_middle()
# list1.display()

# list1.get_by_index(3)
# list1.get_by_value(4)