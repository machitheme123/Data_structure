from avl import AVL
if __name__=='__main__':
    t=AVL()
    t.put(75,'apple')
    t.put(80,'grape')
    t.put(85,'lime')
    t.put(20,'mango')
    t.put(10,'strawberry')
    t.put(50,'banana')
    t.put(30,'cherry')
    t.put(40,'watermelon')
    t.put(70,'melon')
    t.put(90,'plum')
    print('전위순회:\t',end='')
    t.preorder(t.root)
    print('중위순회:\t',end='')
    t.inorder(t.root)

    '''
    print('\n75,85 삭제 후')
    t.delete(75)
    t.delete(85)
    print('전위순회:\t',end='')
    t.preorder(t.root)
    print('중위순회:\t',end='')
    t.inorder(t.root)
    '''