#%%
def bucket_sort(seq):
    # make buckets
    buckets =  [[] for _ in range(len(seq))]
    # assign values
    for value in seq:
        bucket_index = value * len(seq) // (max(seq) + 1)
        buckets[bucket_index].append(value)
    # sort & merge
    sorted_list = []
    for bucket in buckets:
        print("aaaa",sorted_list,quick_sort(bucket))
        sorted_list.extend(quick_sort(bucket))
    return sorted_list
'''
def quick_sort(ARRAY):
    ARRAY_LENGTH = len(ARRAY)
    if( ARRAY_LENGTH <= 1):
        return ARRAY
    else:
        PIVOT = ARRAY[0]
        GREATER = [ element for element in ARRAY[1:] if element > PIVOT ]
        LESSER = [ element for element in ARRAY[1:] if element <= PIVOT ]
        return quick_sort(LESSER) + [PIVOT] + quick_sort(GREATER)
'''
def quick_sort(ARRAY):
    ARRAY_LENGTH = len(ARRAY)
    if( ARRAY_LENGTH <= 1):
        return ARRAY
    else:
        PIVOT = ARRAY[0]
        print('pivot',ARRAY[0])
        GREATER = [ element for element in ARRAY[1:] if element > PIVOT ]
        print('Great',GREATER)
        LESSER = [ element for element in ARRAY[1:] if element <= PIVOT ]
        print('less',LESSER)
        return quick_sort(LESSER) + [PIVOT] + quick_sort(GREATER)
        
#a = [54,88,77,26,93,17,49,10,17,77,11,31,22,44,17,20]
a = [54,88,77,26,93,17,49]
print('정렬 전:\t', a)  
b = bucket_sort(a)
print('정렬 후:\t', b)

#%%

a = [54,88,77,26,93,17,49]

buckets =  [[] for _ in range(len(a))]
buckets

#%%
a=[]
b=[[4],[1]]
a.extend(b)
print(a)

def quick_sort(ARRAY):
    ARRAY_LENGTH = len(ARRAY)
    if( ARRAY_LENGTH <= 1):
        return ARRAY
    else:
        PIVOT = ARRAY[0]
        print('pivot',ARRAY[0])
        GREATER = [ element for element in ARRAY[1:] if element > PIVOT ]
        print(GREATER)
        LESSER = [ element for element in ARRAY[1:] if element <= PIVOT ]
        print(LESSER)
        return quick_sort(LESSER) + [PIVOT] + quick_sort(GREATER)

quick_sort(b)
