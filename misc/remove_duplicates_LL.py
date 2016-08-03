class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
        p = Node(data)        
        if head==None:
            head=p
        elif head.next==None:
            head.next=p
        else:
            start=head
            while(start.next!=None):
                 start=start.next
            start.next=p
        return head 
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next	

    def removeDuplicates(self,head):
        #Write your code here
        
        if head == None:
            return None
        else:
            current = head
            while(current):
                if current.next == None:
                    break
                pointer = current.next
                while pointer:
                    data1 = current.data
                    data2 = pointer.data
                    if data1 != data2:
                        break
                    pointer = pointer.next
                current.next = pointer
                current = pointer

            return head
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)   
head=mylist.removeDuplicates(head)
mylist.display(head);
                