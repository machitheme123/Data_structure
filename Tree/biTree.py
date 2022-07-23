class Node:
    def __init__(self,item,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right

class BinaryTree:
    def __init__(self):
        self.root=None

    def preorder(self,n):#전위순회: 루트부터 시작
        if n!=None:
            print(str(n.item),' ',end='')
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

    def inorder(self,n):#중위순회:왼쪽 맨끝에서 시작, 방문지점 표기
        if n!= None:
            if n.left:
                self.inorder(n.left)
            print(str(n.item),' ',end='')
            if n.right:
                self.inorder(n.right)
                
    def postorder(self,n):#후위순회: 왼쪽 맨끝 시작, 서브트리부터 표기
        if n !=None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(str(n.item),' ',end='')
    
    def levelorder(self,root):#레벨순회
        q=[]
        q.append(root)
        while len(q)!=0:
            t=q.pop(0)
            print(str(t.item),' ',end='')
            if t.left!=None:
                q.append(t.left)
            if t.right!=None:
                q.append(t.right)
    
    def height(self,root):
        if root==None:
            return 0
        return max(self.height(root.left),self.height(root.right))+1
