def selection_sort(a):
    for i in range(0,len(a)-1): 
        minimum=i 
        for j in range(i+1,len(a)): #why not len(a)-1?
            if a[minimum]>a[j]:
                minimum=j
        a[i],a[minimum]=a[minimum],a[i]
'''
ex) a=[2,5,4,7,1]
len(a)=5

a[i]를 기준으로 오른쪽 항목들이랑 크기 비교후
 작으면 min에 저장후 마지막에 위치 교환

1st iteration: i=0,j=0
if 2>2 X
j++

min=0,j=1
if 2>5 X
j++

min=0,j=2
if 2>4 X
j++

min=0,j=3
if 2>7 X
j++

min=0,j=4
if 2>1 O
minimum=4
j++

min=4,j=5
if 1>



'''

a=[2,5,4,7,1]
print(a)
selection_sort(a)
print(a)

