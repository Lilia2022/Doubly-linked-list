# Doubly linked list
# Niharica and Precilia Group

# create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None  # instantiate head pointer

    # create a fuction for adding node at the end of the list
    def add_at_end(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
            new_node.next = None

    # create a function for adding node in front of the list
    def add_in_front(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    # returning the list
    # printing the node at the list
    # checking if the list is empty or not before printing the list

    def print_DLL(self):
        if(self.head == None):
            print("\nEMPTY LIST")
        else:
            current = self.head
            while current:
                # "<--->":is just for showing taht it is a doubly linked list
                print(current.data, "<--->", end=" ")
                current = current.next
        print("\n")

    def is_empty(self):
        if(self.head == None):
            return True
        else:
            return False

    def get_leght(self):
        count = 0
        current = self.head
        while(current != None):
            current = current.next
            count += 1
        return count

    def search(self, key):
        count = 0
        current = self.head
        while(current != None):
            if(current.data == key):
                count += 1
            current = current.next
        return count

    # Creating function for removing a node **in front, **at k-th position of key node,**at the end

    def remove(self, key):
        current = self.head
        #deleting in front
        while(current != None):
            if current.data == key:
                # deleting in the middle at k-th position of key node
                # if current.next:
                if(self.get_leght() == 1):
                    self.remove_front()
                elif(self.get_leght() > 1):
                    nxt = current.next
                    prev = current.prev
                    prev.next = nxt
                    nxt.prev = prev
                    current.next = None
                    current.prev = None
                    current = None
                    return
            current = current.next

    # insertion at k-th position, before the key element
    # position of data = position of key - 1
    def insertion_before_key(self, key, data):
        current = self.head
        while current:
            if current.prev is None and current.data == key:
                self.add_in_front(data)
                return
            elif current.data == key:
                new_node = Node(data)
                prev = current.prev
                prev.next = new_node
                current.prev = new_node
                new_node.next = current
                new_node.prev = prev
            current = current.next

    # reversing the list by introducing temp and reversing pointer
    def reverse(self):
        temp = None
        current = self.head
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp:
            self.head = temp.prev

    def remove_end(self):
        if(self.get_leght() == 0):
            print("List is empty")
            return
        else:
            current = self.head
            if(self.get_leght() == 1):
                self.remove_front()
            else:
                while(current != None):
                    prev = current.prev
                    current = current.next
                prev.next = None
        # current.prev = None
        # current = None

    def remove_front(self):
        if(self.get_leght() == 0):
            print("List is empty")
            return
        else:
            current = self.head
            if not current.next:
                current = None
                self.head = None
                return
                #deleting in front
            else:
                nxt = current.next
                current.next = None
                nxt.prev = None
                current = None
                self.head = nxt
                return

    def del_k(self, key):
        current = self.head
        count = 1
        while(current != None):
            if(count == key):
                if(self.get_leght() == 1):
                    self.remove_front()
                elif(key == self.get_leght()):
                    self.remove_end()
                else:
                    nxt = current.next
                    prev = current.prev
                    prev.next = nxt
                    nxt.prev = prev
                    current.next = None
                    current.prev = None
                    current = None
                    return
            current = current.next
            count += 1

    def ins_k(self, key, data):
        current = self.head
        count = 1
        if key == 1:
            self.add_in_front(data)
            return
        elif key == self.get_leght()+1:
            self.add_at_end(data)
            return
        else:
            while(current != None):
                if(count == key):
                    new_node = Node(data)
                    new_node.next = prev.next
                    new_node.prev = prev
                    prev.next.prev = new_node
                    prev.next = new_node
                    return
                prev = current
                current = current.next
                count += 1

    def del_all_ele(self):
        count = self.get_leght()
        while(count > 0):
            self.remove_front()
            count -= 1
        return


# Here we are going to call all above functions
# intialisation of the doubly linked list
flag = True
while(flag):
    print("-------------------------------")
    print("Menu:")
    print("1.Create a new list")
    print("2.Exit")
    print("--------------------------------")
    choice1 = int(input("Enter input: "))
    if choice1 == 1:
        dll = DLL()  # creating a new linked list
        print("-------------------------------")
        print("Select: ")
        print("1. Print the list")
        print("2. Insert at the front")
        print("3. Insert at the end")
        print("4. Delete at the end")
        print("5. Delete at the front")
        print("6. Delete the key")
        print("7. Insert before key")
        print("8. Length of List")
        print("9. Search a key")
        print("10. Reverse the list")
        print("11. Check list empty or not")
        print("12. remove from k-th position")
        print("13. insert element at k-th position")
        print("14. delete all elements")
        print("15. Exit")
        print("-------------------------------")
        flag2 = True
        while(flag2):
            choice2 = int(input("Enter the choice: "))
            print("\n")
            if(choice2 == 1):
                dll.print_DLL()
            elif(choice2 == 2):
                data1 = input("Enter the data to insert at front: ")
                dll.add_in_front(data1)
            elif(choice2 == 3):
                data2 = input("Enter the data to insert at end: ")
                dll.add_at_end(data2)
            elif(choice2 == 4):
                dll.remove_end()
            elif(choice2 == 5):
                dll.remove_front()
            elif(choice2 == 6):
                data3 = input("Enter the data to be deleted: ")
                dll.remove(data3)
            elif(choice2 == 7):
                data4 = input("Enter the key: ")
                data5 = input("Enter the data: ")
                dll.insertion_before_key(data4, data5)
            elif(choice2 == 8):
                print("Length of the list is: ")
                print(dll.get_leght())
                print("\n")
            elif(choice2 == 9):
                data6 = input("Enter the key to search: ")
                print("Occurence of "+data6)
                print(dll.search(data6))
            elif(choice2 == 10):
                dll.reverse()
            elif(choice2 == 11):
                print(dll.is_empty())
            elif(choice2 == 12):
                data7 = int(input("Enter the kth position: "))
                dll.del_k(data7)
            elif(choice2 == 13):
                data8 = int(input("kth position: "))
                data9 = input("Enter the data: ")
                dll.ins_k(data8, data9)
            elif(choice2 == 14):
                dll.del_all_ele()
            elif(choice2 == 15):
                flag2 = False
            else:
                print("Invalid Input!!!")

    else:
        print("Thankyou!!")
        flag = False
