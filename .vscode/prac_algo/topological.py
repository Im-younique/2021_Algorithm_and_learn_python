from collections import defaultdict
import heapq

def main():
    N, M = map(int, input().split())
    edges = [[] for i in range(N+1)]
    indegree = [0 for i in range(N+1)]

    for i in range(M):
        x, y = map(int, input().split())
        edges[x].append(y)
        indegree[y] += 1
    
    queue = []
    res = []

    for i in range(1, N+1):
        if indegree[i] == 0:
            heapq.heappush(queue, i)

    while queue:
        node = heapq.heappop(queue)
        res.append(node)
        for j in edges[node]:
            indegree[j] -= 1
            if indegree[j] == 0:
                heapq.heappush(queue, j)
    
    print(*res)


if __name__ == '__main__':
    main()