import math

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
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

    def SumTwoLists(self, llist):
        list1 = self.head
        list2 = llist.head
        sum_list = LinkedList()
        carry = 0

        list1 = list1.next
        list2 = list2.next
        while list1 or list2:

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
                sum_list.append(remainder)
            else:
                carry = 0
                sum_list.append(s)
            list1 = list1.next
            list2 = list2.next 
        
        sum_list.display()


    def length(self):
        current_node = self.head
        length = 0
        while current_node.next != None:
            length+=1
            current_node = current_node.next
        return length

    def get(self, index):
        current_index = 0
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            if current_index == index:
                print(current_node.data)
                return current_node.data
            else:
                current_index+=1

    def delete(self, index):
        current_index = 0
        current_node = self.head
        while current_node.next != None:
            prev_node = current_node
            current_node = current_node.next
            if current_index == index:
                prev_node.next = current_node.next
                break
            current_index += 1

    def deleteDups(self):
        current_node = self.head
        hashTable = {}

        while current_node.next != None:
            prev_node = current_node
            current_node = current_node.next
            if current_node.data in hashTable:
                prev_node.next = current_node.next
            else:
                hashTable[current_node.data] = True
    
    def splitList(self):
        if self.length() == 0:
            print("Error Bitch: Try again... There is nothing in the list")
            return
        current_node = self.head
        new_list = self.head
        runner = self.head
        while runner.next != None:
            runner = runner.next
            if runner.next == None:
                break
            runner = runner.next
            current_node = current_node.next
        toReturn = current_node.next
        current_node.next = None;
        return toReturn


    def findLast(self):
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            if current_node.next == None:
                print(current_node.data)
                return current_node.data


    def deleteMiddle(self):
        if self.length() < 2:
            print("Whoa bitch... Thats as far as you go...")
            return
        target_index = round(self.length() / 2)
        current_index = 0
        current_node = self.head
        while current_node.next != None:
            prev_node = current_node
            current_node = current_node.next
            if target_index == current_index:
                prev_node.next = current_node.next
                return
            else:
                current_index += 1

    def returnKth(self, int):
        target = self.length() - int - 1
        current_index = 0
        current_node = self.head

        while current_node.next != None:
            current_node = current_node.next
            if target == current_index:
                print(current_node.data)
                return current_node.data
            current_index += 1
    
    def displayNew(self, newList):
        iterateThis = newList
        elems = []
        while iterateThis.next != None:
            iterateThis = iterateThis.next
            elems.append(iterateThis.data)
        print(elems)
        return elems
        


    # def divideList(self):
    #     target_index = round(self.length() / 2 - 1)
    #     index1 = 0
    #     index2 = 0
    #     current_list1 = self.head
    #     current_list2 = self.head
    #     first_list = self.head
    #     second_list = self.head
    #     while current_list1.next != None:
    #         current_list1 = current_list1.next
    #         if index1 < target_index:
    #             first_list = current_list1.next
    #         index1 += 1
    #     while current_list2.next != None:
    #         current_list2 = current_list2.next
    #         if index2 > target_index:
    #             second_list = current_list2.next
    #         index2 += 1
    #     self.displayNew(second_list)
    #     self.displayNew(first_list)
    #     # self.displayNew(second_list)

        






        
# Lets test
test1 = LinkedList()
test1.append(1)        
test1.append(2)        
test1.append(9)
test1.display()
# test.returnKth(4)

test2 = LinkedList()
test2.append(4)
test2.append(9)
test2.append(6)
test2.display()

test1.SumTwoLists(test2)


