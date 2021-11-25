import heapq

def dijstra(edges, start, last, V, allNode):
    INF = float('inf')
    dist = {}               #비용
    found = {}              #방문여부
    prev = {}
    dst = last              #경로탐색을 위해
    for all in allNode:
        dist[all] = INF
        found[all] = False
        prev[all] = []
    dist[start] = 0         #출발지 비용 0
    found[start] = True     #방문완료
    queue = []
    heapq.heappush(queue, [0, start])

    while queue:
        u = heapq.heappop(queue)
        found[u[1]] = True  #연결된 노드 방문
        for i in edges:     #edges모두 순회
            if u[1] in i:   #키 값이 u[1] (출발지) 인것들 중
                node_weight = list(*i.values())     #node_weight[0]다음노드 / node_weight[1] 비용
                if found[node_weight[0]]:
                    continue
                if dist[node_weight[0]] > dist[u[1]] + node_weight[1]:      #갱신
                    dist[node_weight[0]] = dist[u[1]] + node_weight[1]
                    prev[node_weight[0]] = list(i.keys())[0]                #i의 key값 경로탐색위해
                    heapq.heappush(queue, [dist[node_weight[0]], node_weight[0]])

    result = []
    result.append(last)
    while prev[last]:               #목적지부터 출발지까지 거꾸로 탐색
        result.append(prev[last])
        last = prev[last]
    result = result[::-1]           #목적지부터 출발지까지의 경로이니 뒤집음
    print("".join(result))          #최단경리 경로 출력
    return dist[dst]

def main():
    V, E  = map(int, input().split())
    start, end = map(str, input().split())
    allNode = list(map(str, input().split()))
    edges = []

    for i in range(E):
        n1, n2, c = map(str, input().split())
        edges.append({n1: [n2, int(c)]})        #양방향 그래프
        edges.append({n2: [n1, int(c)]})

    print(dijstra(edges, start, end, V, allNode))

if __name__ == "__main__":
    main()