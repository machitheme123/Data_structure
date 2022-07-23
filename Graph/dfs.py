#%%
adj_list = [[2, 1], [3, 0], [3, 0], [9, 8, 2, 1], 
            [5], [7, 6, 4], [7, 5], [6, 5], [3], [3]]  
N = len(adj_list) # �׷��� ���� ��
visited = [False for x in range(N+1)] # �湮�Ǹ� True��
 
def dfs(v):
    visited[v] = True # ���� v �湮
    print(v, ' ', end='') # ���� v ���
    for w in adj_list[v]: # ���� v�� ������ �� ������ ����
        if not visited[w]: 
            dfs(w) # v�� ������ �湮 �ȵ� ���� ���ȣ��

print('DFS �湮 ����:')     
for i in range(N): 
    if not visited[i]: 
        dfs(i)