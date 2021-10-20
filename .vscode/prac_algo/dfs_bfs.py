def bfs(start_node):
    queue = [start_node]
    visit_list[start_node] = 0      #방문한 점 0으로 표시
    while queue:
        V=queue.pop(0)              #큐 형식으로 빼서 출력
        print(V, end=' ')
        for i in range(1, N+1):     #N은 정점의 갯수 즉, 엣지의 갯수
            if(visit_list[i] == 1 and matrix[start_node][i] == 1):  #방문하지 않은 곳이고, 시작노드와 간선연결 되어있으면 queue에 넣는다.
                queue.append(i)
                visit_list[i] = 0

def dfs(start_node):    #재귀로 dfs 구현
    visit_list[start_node] = 1      #방문한 점 1로 표시
    print(start_node, end=' ')
    for i in range(1, N+1):
        if(visit_list[i] == 0 and matrix[start_node][i] == 1):      #방문하지 않은 곳이고, 시작노드와 간선연결 되어있으면 재귀
            dfs(i)

def my_dfs(start_node): #stack dfs 구현 (좀 다른데..?)
    stack = [start_node]
    visit_list[start_node] = 1      #방문한 점 1로 표시
    while stack:    
        V = stack.pop()             #스택에 저장된 값을 하나씩 빼서 넣는다.
        print(V, end=' ')
        for i in range(1, N+1):
            if(visit_list[i] == 0 and matrix[start_node][i] == 1):  #방문하지 않은 곳이고, 시작노드와 간선연결 되어있으면 stack에 넣는다.
                stack.append(i)
                visit_list[i] = 1

N, M, V = map(int, input().split())     #N : 정점의 개수, M : 간선의 개수 V : 시작 node
matrix = [[0]*(N+1) for i in range(N+1)] #graph를 모두 0으로 채운다.    [0]과 연결되어있는 간선 / [1]과 연결된 간선 [2]와 연결된 간선 [3] --- 모두 0으로 초기화
for i in range(M):
    a, b = map(int, input().split())    #input 값 처리
    matrix[a][b] = matrix[b][a] = 1     #2개씩 들어오는 input은 간선으로 연결되어 있음 표시 1
visit_list=[0]*(N+1)

dfs(V)
print()
bfs(V)


