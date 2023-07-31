class node:
    def __init__(self,data):
        self.data=data 
        self.next=None
class linkedlist:
    def __init__(self,head):
        head.next=None

    def mid_node(self,head):
        c1=head 
        c2=head 
        while c2.next!=None:
            c1=c1.next
            c2=c2.next.next
        return c1

