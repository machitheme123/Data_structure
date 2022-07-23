#%%
import sys
N = 8  # 그래프 정점 수
s = 0  # 시작정점
g = [None for x in range(N+1)]
g[0] = [(1, 1), (3, 2)]
g[1] = [(0, 1), (2, 4), (3, 3), (4, 1), (5, 6)]
g[2] = [(1, 4), (5, 1), (6, 1), (7, 2)]
g[3] = [(0, 2), (1, 3), (4, 5)]
g[4] = [(1, 1), (3, 5), (6, 2)]
g[5] = [(1, 6), (2, 1), (7, 9)]
g[6] = [(2, 1), (4, 2), (7, 1)]
g[7] = [(2, 2), (5, 9), (6, 1)]

visited = [False for x in range(N+1)]  # 초기화
D = [sys.maxsize for x in range(N+1)]  # D[i]를 최댓값으로 초기화
D[s] = 0
previous = [None for x in range(N+1)]  # 최단경로를 추출하기 위해
previous[s] = s

for k in range(N):
    m = -1 #초기화
    min_value = sys.maxsize #초기화
    for j in range(N): # 방문 안된 정점들의 D 원소들 중에서 최솟값을 가진 정점 m 찾기           
        if not visited[j] and D[j] < min_value:
            min_value = D[j]
            m = j           
    visited[m] = True
    for w, wt in g[m]: # m에 인접한 방문 안된 각 정점의 D의 원소 갱신           
        if not visited[w]:  
            if D[m]+wt < D[w]:             
                D[w] = D[m] + wt  # D 원소 갱신
                previous[w] = m

print('정점 ', s,'(으)로부터 최단거리:')
for i in range(N): 
    if D[i] == sys.maxsize:
        print(s,'와(과) ', i ,' 사이에 경로 없음.')
    else:
        print('[%d, %d]'% (s, i), '=', D[i])
        
print('\n정점  ', s,'(으)로부터의 최단 경로')
for i in range(N): 
    back = i
    print(back, end='')
    while back != s: 
        print(' <-', previous[back], end='')
        back = previous[back]
    print()