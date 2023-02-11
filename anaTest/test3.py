import heapq
import sys

def dijkstra(edges, V, E, src, dst, waterList):
    INF = float('inf')
    distance = [INF for _ in range(V + 1)]
    distance[src] = 0
    water = [0 for _ in range(V + 1)]
    waterList.insert(0, 0)
    queue = []
    found = [False for _ in range(V + 1)]
    #초기화 완료

    heapq.heappush(queue, [0, src])     #거리의 비용, 노드 (최소힙 순서)
    water[src] = waterList[src]
    #출발지 노드
    while queue:
        v = heapq.heappop(queue)
        found[v[1]] = True #found shortest path for v[1] (node)
        for node_weight in edges[v[1]]:     #v[1]에 대한 인접노드 방문
            if( found[node_weight[0]]):     #이미 최단경로를 찾은경우
                continue
            if(distance[node_weight[0]] > distance[v[1]] + node_weight[1]):     #distance값 갱신
                distance[node_weight[0]] = distance[v[1]] + node_weight[1]      #갱신
                water[node_weight[0]] = water[v[1]] + waterList[node_weight[0]]
                heapq.heappush(queue, [distance[node_weight[0]], node_weight[0]])   #갱신후 push
    
    return distance[dst], water[dst]

def main():
    V = int(input())        #엣지 갯수
    waterList = list(map(int, sys.stdin.readline().split()))    #뮬의 경로
    E = int(input())        #노드 갯수
    edges = [ [] for _ in range(V+1)]

    for _ in range(E):
        i, j, c = map(int, input().split())
        edges[i].append([j, c])             
    src, dst = map(int, input().split())    #출발지, 목적지
    res1, res2 = dijkstra(edges, V, E, src, dst, waterList)
    if res1 == float('inf'):
        print(-1)
    else:
        print(res1, res2)

if __name__ == '__main__':
    main()