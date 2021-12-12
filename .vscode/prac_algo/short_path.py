import heapq

def dijkstra(edges, end, M):
    INF = float('inf')
    distance = [INF for _ in range(M+1)]
    distance[1] = 0
    queue = []
    found = [False for _ in range(M+1)]

    heapq.heappush(queue, [0, 1])

    while queue:
        v = heapq.heappop(queue)
        found[v[1]] = True
        for node_weight in edges[v[1]]:
            if(found[node_weight[0]]):
                continue
            if(distance[node_weight[0]] > distance[v[1]] + node_weight[1]):
                distance[node_weight[0]] = distance[v[1]] + node_weight[1]
                heapq.heappush(queue, [distance[node_weight[0]], node_weight[0]])

    return distance[end]

def main():
    N, M = map(int, input().split())   #N은 목적지
    edges = [ [] for _ in range(M+1)]
    for i in range(M):
        c1, c2, money = map(int, input().split())
        edges[c1].append([c2, money])
        edges[c2].append([c1, money])

    print(dijkstra(edges, N, M))
   


if __name__ == '__main__':
    main()