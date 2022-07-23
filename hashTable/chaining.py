class Chaining:
    class Node:    
        def __init__(self, key, data, link): # Node 생성자
            self.key   = key
            self.data  = data
            self.next  = link
            
    def __init__(self, size):
        self.M = size           
        self.a = [None for x in range(size+1)]  # 해시테이블
        
    def hash(self, key): # 나눗셈 함수
        return key % self.M

    def put(self, key, data): # 삽입 연산
        i = self.hash(key) # 9

        # a[9]         
        p = self.a[i]
        # p = object
        while p != None:
            if key == p.key:   # 이미 key 존재하면
                p.data = data  # 데이터만 갱신
                return
            p = p.next 
        print('들어가는 값:',self.a[i])
        self.a[i] = self.Node(key, data, self.a[i])
        print('나오는 값:',self.a[i])
    
    def get(self, key): # 탐색 연산
        i = self.hash(key)
        p = self.a[i]
        while p != None:
            if key == p.key:  
                return p.data # 탐색 성공
            p = p.next 
        return None  # 탐색 실패
    
    def print_table(self): # 테이블 출력
        for i in range(self.M):
            print('%2d' % (i), end='')
            p = self.a[i]
            while p != None:
                print('-->[', p.key,',', p.data, ']', end='')
                p = p.next;
            print()

if __name__ == '__main__':
    t = Chaining(13)
    t.put(25, 'grape') 
    '''
    t.put(37, 'apple')    
    t.put(18, 'banana')
    t.put(55, 'cherry')
    t.put(22, 'mango')    
    t.put(35, 'lime')       
    t.put(50, 'orange')
    t.put(63, 'watermelon')
    print('탐색 결과:')
    print('50의 data = ', t.get(50))
    print('63의 data = ', t.get(63))
    print('해시테이블:')
    t.print_table() 
    '''