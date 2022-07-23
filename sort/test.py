def shell_sort(a):
    h=5
    while h>=1:
        for i in range(h,len(a)):
            j=i
            while j>=h and a[j]<a[j-h]:
                a[j],a[j-h]=a[j-h],a[j]
                j-=h
        h//=2
#a=[5,4,3,2,1,0]
a=[10,8,6,20,4,3,22,1,0,15,16]
print(a)
shell_sort(a)
print(a)

#%%
list(reversed(range(1, 4//2+1)))