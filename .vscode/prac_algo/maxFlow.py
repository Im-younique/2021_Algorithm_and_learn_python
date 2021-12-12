from collections import defaultdict

def dfs(source, sink, parent, edge):
    visited = defaultdict(lambda: 0)
    stack = []
    stack.append(source)
    visited[source] = 1
    while stack:
        node = stack.pop()
        for i in edge[node]:            #i는 node에 대한 인접노드 값들이 됨.
            capacity = edge[node][i]
            if visited[i]:
                continue
            if capacity <= 0:           #음의 값으로 빼지다 보면 0보다 작아지는 경우
                continue
            stack.append(i)
            visited[i] = 1
            parent[i] = node
    
    if visited[sink] == 1:
        return 1
    else:
        return 0

def min_flow(source, sink, parent, edge):
    flow = float('INF')
    while sink != source:
        flow = min(flow, edge[parent[sink]][sink])
        sink = parent[sink]
    return flow

def ford_fulkerson(source, sink, edge):
    parent = defaultdict(lambda: -1)
    max_flow = 0
    while dfs(source, sink, parent, edge):
        path_flow = min_flow(source, sink, parent, edge)
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            edge[u][v] -= path_flow
            edge[v][u] += path_flow
            v = parent[v]
        return max_flow


def main():
    N = int(input())        #엣지 갯수
    edge = defaultdict(lambda: defaultdict(int))

    for i in range(N):
        x, y, z = map(str, input().split())
        edge[x][y] = int(z)
        edge[y][x] = int(z)
    print(ford_fulkerson("A", "Z", edge))

if __name__ == "__main__":
    main()