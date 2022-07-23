#%%
#adj_list = [[3], [6, 10], [7, 11], [0, 6, 8], [13], [14], 
#            [1, 3, 8, 10, 11], [2, 11], [3, 6, 10, 12], 
#            [13], [1, 6, 8], [2, 6, 7], [8], [4, 9], [5]]
adj_list = [[2, 1], [3, 0], [3, 0], [9, 8, 2, 1], 
            [5], [7, 6, 4], [7, 5], [6, 5], [3], [3]]  
N = len(adj_list) # 그래프 정점 수
CCList = []
visited = [False for x in range(N+1)] # 방문되면 True로
 
def dfs(v):
    visited[v] = True # 정점 v 방문
    cc.append(v)
    for w in adj_list[v]: # 정점 v에 인접한 각 정점에 대해
        if not visited[w]:
            dfs(w) # v에 인접한 방문 안된 정점 재귀호출
            
for i in range(N):
    if not visited[i]:
        cc = []
        dfs(i)
        CCList.append(cc)

print('연결성분 리스트:')
print(CCList)