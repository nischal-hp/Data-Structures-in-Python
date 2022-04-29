class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

# Main Utility functions are insert_at, remove_at and also (print, length_ll), which does the required work.
class LinkedList:
    def __init__(self):
        self.head=None

    def print(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr+=str(itr.data) + '-->'
            itr=itr.next
        print(llstr)
            

    def insert_at_beginning(self,data):
        node=Node(data,self.head)  # Point address to the current head location of LL
        self.head=node   # Make the new node as the head of LL
    
    def insert_at_end(self,data):
        if self.head is None:    # Case where there is no element in LL
            node=Node(data,None)
            self.head=node
            return 
        node=Node(data,None)
        itr=self.head
        while itr.next:      # Iterate through LL till the last element is reached 
            itr=itr.next
        itr.next=node

    def create_ll_from_list(self,data_list):  # To Create a LL when an array of Data is passed to it
        for element in data_list:
            self.insert_at_end(element)
    
    def length_ll(self): # To get no. of elements in LL
        itr = self.head
        count=0
        while itr:
            count+=1
            itr=itr.next
        print(count)
        return count

    def remove_at(self,index): # To remove an element from a given index position
        itr=self.head
        curr_index=0
        prev=None
        if index<0 or index>ll.length_ll()-1:
            raise Exception("Invalid Index")
        if index == 0:  # If first element to be removed
            self.head = self.head.next
            return 

        if curr_index==index:
            self.head=None
        while itr and curr_index<index:
            if curr_index == index - 1:  # Stop at the element which is one less than the element to be deleted.
                itr.next=itr.next.next
                break
            curr_index+=1
            itr=itr.next

    def insert_at(self,index,value): # Insert the given value at the given index.
        node=Node(value,None)
        if index<0 or index>ll.length_ll():  # Shouldn't put length-1 here, coz we can add an element at the last location too.
            raise Exception("Invalid Index")
        if index==0:
            node.next=self.head
            self.head=node
            return
        itr=self.head
        count=0
        while itr:
            if count==index-1:  # Index has to start from 1. Otherwise 0-1 becomes -1 which can't be compared with count.
                node.next=itr.next
                itr.next=node
                break
            itr=itr.next
            count+=1
        return

        

if __name__=='__main__':
    ll = LinkedList()
    # ll.insert_at_beginning(5)
    # ll.insert_at_beginning(6)
    # ll.insert_at_end(7)
    ll.create_ll_from_list([1,2,3])
    ll.insert_at(4,4)
    ll.print()
