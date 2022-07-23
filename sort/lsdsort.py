#%%
def lsd_sort(a):
    WIDTH = 3  # 스트링의 문자 수
    N = len(a) # 입력 크기
    R = 128    # radix 크기
    temp = [None] * N
    for d in reversed(range(WIDTH)): # d번째 문자 처리 , d  =2, 1, 0    
        count = [0] * (R+1)
        print(count)
        for i in range(N): # 빈도수 계산
            count[ord(a[i][d])+1] += 1  # ord() 인자의 unicode 값 리턴    
        for j in range(1, R): # 빈도수 누적 계산  
            count[j] += count[j-1]   

        print('count:',count)     
        for i in range(N): # data 복사
            p = ord(a[i][d])
            temp[count[p]] = a[i]
            count[p] +=  1 # 중복되는 경우 temp의 index 이동
        for i in range(N): # t를 a로 복사 
            a[i] = temp[i]
        print('%d번째 문자:\t ' % d, end='')
        for x in a: print(x, ' ', end='')
        print()
        
#a = ['ICN', 'SFO', 'LAX', 'FRA', 'SIN', 'ROM', 'HKG', 'TLV', 
#     'SYD', 'MEX', 'LHR', 'NRT', 'JFK', 'PEK', 'BER', 'MOW']

a= ['213','435','111','301']
print('정렬 전:\t\t ', end='')
for x in a: 
    print(x, ' ', end='')
print()
lsd_sort(a)



#%%
def lsd_sort(a):
    WIDTH = 3  # 스트링의 문자 수
    N = len(a) # 입력 크기
    R = 128    # radix 크기
    temp = [None] * N
    for d in reversed(range(WIDTH)): # d번째 문자 처리 , d  =2, 1, 0    
        count = [0] * (R+1)
        for i in range(N): # 빈도수 계산
            count[ord(a[i][d])+1] += 1  # ord() 인자의 unicode 값 리턴 
        for j in range(1, R): # 빈도수 누적 계산  
            count[j] += count[j-1]        
        for i in range(N): # data 복사
            p = ord(a[i][d])
            temp[count[p]] = a[i]
            count[p] +=  1
        for i in range(N): # t를 a로 복사 
            a[i] = temp[i]
        print('%d번째 문자:\t ' % d, end='')
        for x in a: print(x, ' ', end='')
        print()
        
#a = ['ICN', 'SFO', 'LAX', 'FRA', 'SIN', 'ROM', 'HKG', 'TLV', 
#     'SYD', 'MEX', 'LHR', 'NRT', 'JFK', 'PEK', 'BER', 'MOW']

a= ['219','435','111']
print('정렬 전:\t\t ', end='')
for x in a: 
    print(x, ' ', end='')
print()
lsd_sort(a)

#%%

WIDTH = 3  # 스트링의 문자 수
N = len(a) # 입력 크기
R = 58    # radix 크기
temp = [None] * N
count = [0] * (R+1)
d=2
count=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0]

for i in range(N): # data 복사
            p = ord(a[i][d])
            temp[count[p]] = a[i]
            count[p] +=  1
#print(count)

            
a= ['213','435','111']