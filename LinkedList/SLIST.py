#%%
class EmptyError(Exception):
        pass
class Slist:
    class Node: #노드 생성자
        def __init__(self, item, link):
            self.item=item 
            self.next=link 

    def __init__(self): #단순연결리스트 생성자
        self.head=None
        self.size=0

    def size(self): #size 구하는것
        return self.size

    def is_empty(self): #size가 0인지 확인
        return self.size==0
    
    def insert_front(self,item):
        if self.is_empty():
            self.head=self.Node(item,None)
        else:
            self.head=self.Node(item,self.head) 
            #기존 self.head에 있던 레퍼런스를 새 노드 링크에 넣고, 새 노드의 레퍼런스를 헤드에 재정의
        self.size+=1
    def insert_after(self,item,p):
        p.next=self.Node(item,p.next)
        self.size+=1
    
    def delete_front(self):
        if self.is_empty():
            raise EmptyError('Underflow')
        else:
            self.head=self.head.next
            self.size-=1
    
    def delete_after(self,p):
        if self.is_empty():
            raise EmptyError('Underflow')
        t=p.next
        p.next=t.next
        self.size-=1

    def search(self,target):
        p=self.head
        for k in range(self.size):
            if target==p.item: 
                return k
            p=p.next
        return None
    
    def print_list(self):
        p=self.head
        while p:
            if p.next!=None:
                print(p.item,' -> ',end='')
            else:
                print(p.item)
            p=p.next
#%%
s=Slist()
s.insert_front('orange')
s.insert_front('apple')
s.insert_after('cherry',s.head.next)
s.insert_front('pear')
s.print_list()
print('cherry는 %d 번째' %s.search('cherry'))
print('kiwi는 ',s.search('kiwi'))
