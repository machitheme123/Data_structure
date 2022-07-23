#%%
#adj_list = [[1], [3, 4], [0, 1], 
#            [6], [5], [7], [7], [8], []]  
adj_list = [[],[0],[1],[1],[3],[4],[5,2]]
N = len(adj_list) # 그래프 정점 수
visited = [False for x in range(N+1)] # 방문되면 True로
s = []

def dfs(v):
    visited[v] = True  # 정점 v 방문
    for w in adj_list[v]: # 정점 v에 인접한 각 정점에 대해
        if not visited[w]:
            dfs(w)  # v에 인접한 방문 안된 정점 재귀호출
    s.append(v) # i에서 진출하는 간선이 더 이상 없으므로 i를 s에 추가 

for i in range(N):    
    if not visited[i]:
        dfs(i)
print(s)
s.reverse()
print('위상정렬:')
print(s)