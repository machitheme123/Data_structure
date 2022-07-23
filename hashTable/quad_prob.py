class QuadProbing: 
    def __init__(self, size): # 생성자
        self.M = size 
        self.a = [None for x in range(size+1)] # 해시테이블
        self.d = [None for x in range(size+1)] # key관련 데이터 저장
        self.N = 0  # 항목 수

    def hash(self, key): # 나눗셈 함수
        return key % self.M
    
    def put(self, key, data): # 삽입 연산
        initial_position = self.hash(key) # 초기 위치 
        i = initial_position
        j = 0
        while True:  
            if self.a[i] == None: # 삽입 위치 발견
                self.a[i] = key   # key를 해시테이블에 저장
                self.d[i] = data  # key관련 데이터 저장 
                self.N += 1
                return           
            if self.a[i] == key:  # 이미 key 존재하면
                self.d[i] = data  # 데이터만 갱신
                return  
            j += 1                      
            i = (initial_position + j*j) % self.M # i의 다음 위치  
            if self.N > self.M: # 테이블이 full이면  
                break         
           
    def get(self, key): # 탐색 연산
        initial_position = self.hash(key)
        i = initial_position
        j = 1
        while self.a[i] != None: # a[i]가 비어있지 않으면
            if self.a[i] == key:
                return self.d[i] # 탐색 성공
            i = (initial_position + j*j) % self.M  # i의 다음 위치
            j += 1
        return None # 탐색 실패
    
    def print_table(self): # 해시테이블 출력
        for i in range(self.M):
            print('{:4}'.format(str(i)), ' ', end='')
        print()
        for i in range(self.M):
            print('{:4}'.format(str(self.a[i])), ' ', end='')
        print()
    