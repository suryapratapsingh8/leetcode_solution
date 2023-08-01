class node:
    def __init__(self,data):
        self.data=data 
        self.next=None
class linkedlist:
    def __init__(self,head):
        head.next=None

    def reverse(self):
        prev=None
        current=self.head 
        while(current is not None):
            next=current.next
            current.next=prev 
            prev=current
            current=next 
        self.head=prev

    def add_node(self,newnode):
        newdata=node(newnode)
        newdata=self.head 
        self.head=newdata
