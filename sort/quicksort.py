def qsort(a, low, high):
    if low < high:
        pivot = partition(a,low,high)
        qsort(a, low, pivot-1)
        qsort(a, pivot+1, high)

def partition(a, pivot, high):
    i = pivot + 1
    j = high
    while True:
        while i < high and a[i] < a[pivot]:
            i += 1
        while j > pivot and a[j] > a[pivot]:
            j -= 1
        if j <= i:
            break
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    a[pivot], a[j] = a[j], a[pivot]
    return j

a = [54,88,77,26,93,17,49,10,17,77,11,31,22,44,17,20]
print('정렬 전:\t', a)  
qsort(a, 0, len(a)-1)
print('정렬 후:\t', a)

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
        sorted_list.extend(quick_sort(bucket))
    return sorted_list

def quick_sort(ARRAY):
    ARRAY_LENGTH = len(ARRAY)
    if( ARRAY_LENGTH <= 1):
        return ARRAY
    else:
        PIVOT = ARRAY[0]
        GREATER = [ element for element in ARRAY[1:] if element > PIVOT ]
        LESSER = [ element for element in ARRAY[1:] if element <= PIVOT ]
        return quick_sort(LESSER) + [PIVOT] + quick_sort(GREATER)

        
a = [54,88,77,26,93,17,49,10,17,77,11,31,22,44,17,20]
print('정렬 전:\t', a)  
b = bucket_sort(a)
print('정렬 후:\t', b)
