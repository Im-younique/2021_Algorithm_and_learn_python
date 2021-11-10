import heapq

def prim(edges, N):
    queue = []
    heapq.heappush(queue, [0, 0, 1])        #가상 가상 (첫 노드)

    visit = [ False for _ in range(N+1)]        #방문한 노드
    result = []         #edge정보 저장
    sum = 0

    while queue:
        # h[0]: link cost , h[1]: 현재노드, h[2]: 다음 노드
        h = heapq.heappop(queue)
        if visit[h[2]] == True:
            continue
        else:
            visit[h[2]] = True
            sum += h[0]
            result.append([h[1], h[2], h[0]])       #출력하기 위한 순서

        for e in edges[h[2]]:                       #갱신
            if (visit[e[0]]): continue              #e[0]가 다음노드의 값
            heapq.heappush(queue, [e[1], h[2], e[0]])   #e[1]에는 cost
    return sum, result

def main():
    N = int(input())
    M = int(input())

    edges = [ [] for _ in range(N+1)]

    for _ in range(M):
        u, v, c = map(int, input().split())
        edges[u].append([v, c])             #인접리스트
        edges[v].append([u, c])             #무방향이라 반대까지
    print(prim(edges, N))

if __name__ == "__main__":
    main()