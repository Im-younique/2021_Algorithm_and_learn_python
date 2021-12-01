#ford-fulkerson
from collections import defaultdict
from sys import path

def dfs(start, end, parent, edges):         #dfs에 의한 탐색
    visited = defaultdict(lambda: 0)
    stack = []
    stack.append(start)
    visited[start] = 1
    while stack:
        node = stack.pop()
        for i in range(len(edges[node])):   #인접노드 방문
            capacity = edges[node][i]
            if visited[i]:
                continue
            if capacity <= 0:               #반대 방향 노드의 값이 커짐으로 인해 0보다 작아지면 방문 x
                continue
            stack.append(i)
            visited[i] = 1
            parent[i] = node                #방문 순서 기억하기 위함.

    if visited[end] == 1:
        return 1
    else:
        return 0

def min_flow(start, end, parent, edges):
    flow = float("INF")
    while end != start:                     #목적지로 부터 시작점까지 즉, 반대방향으로 탐색
        flow = min(flow, edges[parent[end]][end])   #기존 flow과 capacity가 작은값 중 저장
        end = parent[end]   #시작점으로 가기 위함
    return flow

def ford_fulkerson(start, end, edges):
    parent = defaultdict(lambda: 0)
    max_flow = 0
    while dfs(start, end, parent, edges):   #임의의 경로 선택
        path_flow = min_flow(start, end, parent, edges)
        max_flow += path_flow       #리턴해야하는 최대값
        v = end
        while v != start:
            u = parent[v]
            edges[u][v] -= path_flow    #순방향은 줄고 반대방향은 늘어나는 구조
            edges[v][u] += path_flow    #반대방향 간선을 위해
            v = parent[v]               #다음 노드로 이동
    
    return max_flow

def main():
    N = int(input())
    edges = []

    for i in range(N):
        edges.append(list(map(int, input().split())))

    start_node = 0
    end_node = N-1

    print(ford_fulkerson(start_node, end_node, edges))

if __name__ == '__main__':
    main()