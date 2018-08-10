class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def addToListForward(self, data):
        new_node = Node(data)
        current_head = self.head

        prev_node = current_head
        current_head = current_head.next

        prev_node.next = new_node
        new_node.next = current_head
        
    def addToListBackward(self, data):
        new_node = Node(data)
        current_node = self.head

        while current_node:
            if current_node.next == None:
                break
            current_node = current_node.next
        current_node.next = new_node

    def display(self):
        elems = []
        current_node = self.head

        while current_node:
            current_node = current_node.next
            elems.append(current_node.data)
            if current_node.next == None:
                break
        print(elems)
        return elems

    def length(self):
        current_head = self.head
        length = 0
        while current_head:
            current_head = current_head.next
            length += 1
            if current_head.next == None:
                break
        print(length)
        return length

    def get(self, index): #could also be the "get Kth Element"
        current_head = self.head
        current_idx = 0

        while current_head:
            current_head = current_head.next
            if index == current_idx:
                print(current_head.data)
                return current_head.data
            else:
                current_idx += 1
            if current_head.next == None:
                break

    def delete(self, index):
        current_head = self.head
        current_idx = 0

        while current_head:
            prev_node = current_head
            current_head = current_head.next
            if index == current_idx:
                print(current_head.data)
                prev_node.next = current_head.next
                return
            else:
                current_idx += 1
            if current_head.next == None:
                break
    
    def deleteDups(self):
        current_node = self.head
        hashTable = {}

        while current_node:
            prev_node = current_node
            current_node = current_node.next
            if current_node.data in hashTable:
                prev_node.next = current_node.next
            else:
                hashTable[current_node.data] = True
            if current_node.next == None:
                break

    def deleteMiddle(self):
        current_node = self.head
        target = round(self.length() / 2)
        current_idx = 0
        while current_node:
            prev_node = current_node
            current_node = current_node.next
            if target == current_idx:
                prev_node.next = current_node.next
                break
            else:
                current_idx += 1
            if current_node.next == None:
                break

    def findLastNode(self):
        current_node = self.head
        while current_node:
            current_node = current_node.next
            if current_node.next == None:
                print(current_node.data)
                return current_node.data

    def splitList(self):
        current_node = self.head
        runner = self.head

        while runner:
            if runner.next != None:
                runner = runner.next
            else:
                break
            runner = runner.next
            current_node = current_node.next
        toReturn = current_node.next
        current_node.next = None
        return toReturn

    def sumList(self, list2):
        list1 = self.head
        list2 = list2.head
        new_list = LinkedList()
        carry = 0
        list1 = list1.next
        list2 = list2.next    

        while list1 or list2:
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
                new_list.addToListForward(remainder)
            else:
                carry = 0
                new_list.addToListForward(s)
            if not list1 and not list2 and carry > 0:
                new_list.addToListForward(carry)
                break

        new_list.display()
        return new_list


# A -> B -> C -> D -> 0
# D -> C -> B -> A -> 0
#

    def reverse_list(self):

        prev = None
        current_node = self.head

        while current_node:
            nxt = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = nxt
        self.head = prev


rev = LinkedList()
rev.addToListForward('A')
rev.addToListForward('B')
rev.addToListForward('C')
rev.display()
rev.reverse_list()
rev.display()

rev2 = LinkedList()
rev2.addToListBackward('A')
rev2.addToListBackward('B')
rev2.addToListBackward('C')
rev2.display()
rev2.reverse_list()
rev2.display()
     





# list1 = LinkedList()
# list1.addToListForward(8)
# list1.addToListForward(2)
# list1.addToListForward(3)
# list1.addToListForward(3)
# list1.addToListForward(3)
# list1.display()
# list1.length()
# list1.get(0)
# list1.delete(0)
# list1.deleteDups()
# list1.display()
# list1.findLastNode()
# list1.splitList()
# list1.display()


# list2 = LinkedList()
# list2.addToListBackward(9)
# list2.addToListBackward(2)
# list2.addToListBackward(3)
# list2.display()
# list2.length()
# list2.get(0)
# list2.delete(0)
# list2.deleteDups()
# list2.display()
# list2.deleteMiddle()
# list2.display()
# list2.findLastNode()
# list2.splitList()
# list2.display()
# list1.sumList(list2)


########################################################################################
# ABOVE THIS LINE IS THE DAILY ROUTINE OF BUILDING THESE ALGORITHMS FROM MEMORY MOSTLY
# BUT I STILL GET STUCK AND NEED TO THINK THESE OUT. EVEN THOUGH I HAVE TO TAKE TIME, I 
# STILL LEARN HOW EACH ALGO OPERATES. ITS ABOUT PRACTICE AND ESTABLISHING A TRAIN OF THOUGHT
# WHEN DEALING WITH THE LINKED LISTS... 

# BELOW THIS WILL BE NEW CONCEPTS LEARNING TODAY...
# 1.	Palindrome
# 2.	Palindrome permutations
# 3.	Reversing a linked list
########################################################################################





