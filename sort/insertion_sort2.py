def insertion_sort(a):
    for i in range(1,len(a)): #why 1번부터?
        for j in range(i,0,-1):
            if a[j-1]>a[j]:
                a[j],a[j-1]=a[j-1],a[j]

a=[54,88,77,26,93]
print(a)
insertion_sort(a)
print(a)