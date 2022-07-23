def selecsort(a):
    for i in range(0,len(a)-1):
        minimum=i
        for j in range(i+1,len(a)-1):
            if a[minimum]>a[j]:
                minimum=j
        spare=a[i]
        a[i]=a[minimum]
        a[minimum]=spare

        
a=[2,5,4,7,1]
print(a)
selecsort(a)
print(a)
