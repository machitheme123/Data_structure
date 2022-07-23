class Node:
    def __init__(self, key, value, left=None, right=None): # 노드 생성자
        self.key   = key
        self.value = value 
        self.left  = left 
        self.right = right 

class BST:           
    def __init__(self): # 트리 생성자
        self.root = None 

    def get(self, k): # 탐색 연산
        return self.get_item(self.root, k)
    
    def get_item(self, n, k):
        if n == None:
            return None # key를 발견 못함
        if n.key > k: # 왼쪽 서브트리 탐색
            return self.get_item(n.left, k)
        elif n.key < k: # 오른쪽 서브트리 탐색 
            return self.get_item(n.right, k) 
        else:
            return n.value # key를 가진 노드 발견

    def put(self, key, value): # 삽입 연산
        self.root = self.put_item(self.root, key, value)
        
    def put_item(self, n, key, value):
        if n == None:
            return Node(key, value) 
        if n.key > key: # 왼쪽 서브트리에 삽입
            n.left = self.put_item(n.left, key, value)
        elif n.key < key: # 오른쪽 서브트리에 삽입
            n.right = self.put_item(n.right, key, value) 
        else: # 노드 n의 value 갱신
            n.vlaue = value
        return n

    def delete_min(self): # 최솟값 삭제
        if self.root == None:
            print('트리가 비어 있음')
        self.root = self.del_min(self.root)
        
    def del_min(self, n):
        if n.left == None:
            return n.right  # n의 오른쪽자식 리턴
        n.left = self.del_min(n.left) # n의 왼쪽자식으로 재귀호출
        return n

    def delete(self, k): # 삭제 연산
        self.root = self.del_node(self.root, k)
         
    def del_node(self, n, k):
        if n == None:
            return None
        if n.key > k: # 왼쪽자식으로 이동
            n.left = self.del_node(n.left, k)   
        elif n.key < k: # 오른쪽자식으로 이동
            n.right = self.del_node(n.right, k) 
        else: # 삭제할 노드 발견
            if n.right == None: # case 0, 1
                return n.left   
            if n.left == None:  # case 1
                return n.right 
            target = n          # case 2, Line 66-69          
            n = self.minimum(target.right) # 중위 후속자를 찾아서 n이 참조하게 함
            n.right = self.del_min(target.right)
            n.left  = target.left
        return n
    
    def min(self): # 최솟값 가진 노드 찾기
        if self.root == None:
            return None
        return self.minimum(self.root)
    
    def minimum(self, n):
        if n.left == None:
            return n
        return self.minimum(n.left)
    
    def preorder(self, n): # 전위순회
        if n != None:
            print(str(n.key),' ', end='')
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)
 
    def inorder(self, n): # 중위순회
        if n != None:
            if n.left:
                self.inorder(n.left)
            print(str(n.key),' ', end='')
            if n.right:
                self.inorder(n.right)

    def postorder(self, n): # 후위순회
        if n != None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(str(n.key),' ', end='')
              
    def levelorder(self, root): # 레벨순회
        q = []
        q.append(root)
        while len(q) != 0:  
            t = q.pop(0) 
            print(str(t.key), ' ', end='')
            if t.left != None: 
                q.append(t.left)  
            if t.right != None: 
                q.append(t.right)