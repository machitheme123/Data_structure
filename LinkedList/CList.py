class EmptyError(Exception):
    pass
class CList:
    class Node:
        def __init__(self,item,link):
            self.item=item
            self.next=link
    def __init__(self):
        self.last=None
        self.size=0
    def no_items(self): return self.size
    def is_empty(self): return self.size==0

    def insert(self,item):
        n=self.Node(item,None)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
        self.size+=1
    