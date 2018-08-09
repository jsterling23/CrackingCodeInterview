class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()


    def append(self, data):
        current_node = self.head
        new_node = Node(data)

        prev_node = current_node
        current_node = current_node.next

        prev_node.next = new_node
        new_node.next = current_node

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

    def SumTwoLists(self, list2):
        list1 = self.head    
        list2 = list2.head
        sum_list = LinkedList()
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
                sum_list.append(remainder)
            else:
                carry = 0
                sum_list.append(s)
            if list1 == None and carry > 0:
                sum_list.append(carry)
            elif list2 == None and carry > 0:
                sum_list.append(carry)
                
        sum_list.display()

    def length(self):
        current_node = self.head
        length = 0
        while current_node:
            if current_node.next == None:
                break
            length += 1
            current_node = current_node.next
        return length

    def get(self, index):
        if index > self.length() - 1:
            print("Error Bitch!")
            return
        elif index < 0:
            print('Like... wtf are you doing?')
            return
        current_node = self.head
        function_index = 0

        ######## ONE WAY TO DO THE OPERATIONS
        while current_node.next != None:
            current_node = current_node.next
            if function_index == index:
                print(current_node.data)
                return current_node.data
            else:
                function_index += 1


        ######## SECOND WAY TO DO THE OPERATION
        # while current_node:
        #     if current_node.next == None:
        #         break
        #     current_node = current_node.next
        #     if index == function_index:
        #         print("Data: ", current_node.data)
        #     function_index += 1


    def delete(self, index):
        current_node = self.head
        idx = 0

        ######## ONE WAY TO DO THE OPERATIONS
        # while current_node.next != None:
        #     prev_node = current_node
        #     current_node = current_node.next
        #     if index == idx:
        #         prev_node.next = current_node.next
        #         break
        #     else:
        #         idx += 1

        ######## SECOND WAY TO DO THE OPERATION
        while current_node:
            prev_node = current_node
            current_node = current_node.next
            if index == idx:
                prev_node.next = current_node.next
                break
            else:
                idx += 1

        
    
    def deleteDups(self):
        current_node = self.head
        hashTable = {}

        ####### ONE WAY TO DO THIS
        # while current_node:
        #     if current_node.next == None:
        #         break
        #     prev_node = current_node
        #     current_node = current_node.next
        #     print('current node data: ', current_node.data)
        #     if current_node.data in hashTable:
        #         prev_node.next = current_node.next
        #     else:
        #         hashTable[current_node.data] = True

        ####### ANOTHER WAY TO DO THIS
        while current_node.next != None:
            prev_node = current_node
            current_node = current_node.next
            if current_node.data in hashTable:
                prev_node.next = current_node.next
            else:
                hashTable[current_node.data] = True


    def splitList(self):
        current_node = self.head
        runner = self.head


        ####### ONE WAY TO DO IT
        # while runner:
        #     if runner.next != None:
        #         runner = runner.next
        #     else:
        #         break
        #     runner = runner.next
        #     current_node = current_node.next
        # returnList = current_node.next
        # current_node.next = None;
        # return returnList

        ####### ANOTHER WAY TO DO IT
        while runner.next != None:
            runner = runner.next
            if runner.next == None:
                break
            runner = runner.next
            current_node = current_node.next

        returnList = current_node.next
        current_node.next = None;
        return returnList


    def findLast(self):
        current_node = self.head
        
        ####### ONE WAY TO DO IT
        # while current_node:
        #     if current_node.next == None:
        #         print(current_node.data)
        #         return current_node.data
        #     else:
        #         current_node = current_node.next
    
        ####### ANOTHER WAY TO DO IT
        while current_node.next != None:
            current_node = current_node.next
            if current_node.next == None:
                print(current_node.data)
                return current_node.data
            


    def deleteExactMiddle(self):
        target = round(self.length() / 2)
        index = 0
        current_node = self.head

        ####### ONE WAY TO DO IT
        while current_node.next != None:
            prev_node = current_node
            current_node = current_node.next
            if index == target:
                prev_node.next = current_node.next
                return
            else:
                index += 1

    # def returnKth(self, target): this is the same as my get()



        
                





llist1 = LinkedList()
llist1.append(1)
llist1.append(1)
llist1.append(1)
llist1.append(1)
llist1.display()

llist2 = LinkedList()
llist2.append(9)
llist2.append(1)
llist2.append(1)
llist2.append(1)
llist2.display()

llist1.SumTwoLists(llist2)
