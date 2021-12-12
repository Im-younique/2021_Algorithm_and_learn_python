from collections import defaultdict, deque
INF = float('INF')

def bfs(source, sink, parent, edge):
    visited = defaultdict(lambda: 0)
    queue = deque()
    queue.append(source)
    visited[source] = 1             #시작노드 방문
    while queue:
        u = queue.popleft()
        for i in edge[u]:           #edge의 인접노드 찾기
            capacity = edge[u][i]   #인접노드의 capacity
            if visited[i]:          #방문했으면 방문할 필요 x
                continue
            if capacity <= 0:       #cpacity가 줄어서 방문 할 수 없는 상태
                continue
            queue.append(i)         #다음 방문을 위해 queue에 넣는다.
            visited[i] = 1          #방문한 값 입력
            parent[i] = u           #경로저장

    if visited[sink]:   #sink를 찾은경우
        return 1
    else:
        return 0

def min_flow(source, sink, parent, edge):
    flow = INF          #초기화
    while sink != source:           #sink노드로 부터 차례차례 살펴본다
        flow = min(flow, edge[parent[sink]][sink])      #기존flow보다 capacity가 작은값을 저장
        sink = parent[sink]         #다음 sink노드가 이동
    return flow

def ford_fulkerson(source, sink, edge):     #임의의 경로를 선택
    parent = defaultdict(lambda: -1)        #sink부터 source까지 거꾸로 찾는
    max_flow = 0
    while bfs(source, sink, parent, edge):  #임의의 경로를 bfs로 찾음
        path_flow = min_flow(source, sink, parent, edge)    #경로의 최소값
        max_flow += path_flow               #리턴해야하는 최대값
        v = sink
        while v != source:                  #거꾸로 찾음
            u = parent[v]                   #이웃노드
            edge[u][v] -= path_flow         #capacity값 update
            edge[v][u] += path_flow         #순방향은 줄고 반대방향은 늘어남
            v = parent[v]                   #다음 노드로 이동
        return max_flow 



def main():
    n = int(input())            #엣지 갯수 입력
    s, t = map(str, input().split())    #source, sink node t 입력
    edge = defaultdict(lambda: defaultdict(int))    #사전으로 정의 초기화

    for _ in range(n):          #엣지 값 입력
        i, j, c = map(str, input().split())
        edge[i][j] += int(c)
        edge[j][i] += int(c)
    print(ford_fulkerson(s, t, edge))
        