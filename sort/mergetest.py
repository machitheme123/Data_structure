original=[1,4,6,3,5,8,9]
a=[3,5,8,9]
b=[1,4,6]


def merge(a, b, low, mid, high):
        i = low
        j = mid+1
        for k in range(low, high+1): # a의 앞/뒷부분을 합병하여 b에 저장
            if i > mid:             
                b[k] = a[j] # 앞부분이 먼저 소진된 경우
                j += 1
            elif j > high:
                b[k] = a[i] # 뒷부분이 먼저 소진된 경우
                i += 1
            elif a[j] < a[i]:
                b[k] = a[j] # a[j]가 승자
                j += 1
            else:
                b[k] = a[i] # a[i]가 승자
                i += 1
        for k in range(low, high+1):
            a[k] = b[k]  # b를 a에 복사  