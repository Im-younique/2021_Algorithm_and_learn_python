def bellmanFord(V, edges, src, dest, allNode):
    INF = float('inf')
    distance = [INF for _ in range(V+1)]        #모든거리 INF로 초기화
    distance[src] = 0                           #시작지점의 거리 0
    route = {}
    for v in range(V):
        route[allNode[v]] = []
        
    for i in range(V-1):
        for source, dst, weight in edges:       #source = edges[0], dst = edges[1], weight = edges[2] 
            if distance[dst] > distance[source] + weight:       #갱신
                distance[dst] = distance[source] + weight
                route[allNode[dst-1]] = allNode[source -1]      #갱신된 {목적지: 출발지} 알파벳 형태 (경로저장)
    for source, dst, weight in edges:           #음수 순환 경우 / 최단거리 찾을 수 없음.
        if distance[dst] > distance[source] + weight:
            print("Negative")
            return 0
    result = []
    cur = allNode[dest-1]
    while cur != allNode[src - 1]:      #목적지 ~ 출발지 경로 탐색
        result.append(cur)
        cur = route[cur]
    result.append(allNode[src - 1])
    result.reverse()
    for i in range(len(result)-1):      #경로 당 비용출력
        for source, dst, weight in edges:
            if allNode[source - 1] == result[i] and allNode[dst-1] == result[i+1]:
                print(allNode[source-1], allNode[dst-1], weight)
                
def main():
    N, M = map(int, input().split())
    src, dst = input().split()
    allNode = list(input().split())
    edges = []
    src = allNode.index(src) + 1
    dst = allNode.index(dst) + 1
    for _ in range(M):                  #각 노드별로 index값에 맞춰 숫자로 부여
        i, j, c = input().split()
        i = allNode.index(i)+1
        j = allNode.index(j)+1
        c = int(c)
        edges.append([i, j, c])
    bellmanFord(N, edges, src, dst, allNode)
    
if __name__ == '__main__':
    main()