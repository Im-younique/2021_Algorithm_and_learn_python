def main():
    # N, M = map(int, input().split()) #N은 목적지이자, 노드의 갯수
    # INF = float('inf')
    # edges = [[INF for i in range(N+1)] for i in range(N+1)]
    # for i in range(M):
    #     x, y, c = map(int, input().split())
    #     edges[x][y] = c
    #     edges[y][x] = c

    # for k in range(N):
    #     for i in range(1, N+1):
    #         for j in range(1, N+1):
    #             if edges[i][j] > edges[i][k] + edges[k][j]:
    #                 edges[i][j] = edges[i][k] + edges[k][j]

    # print(edges[1][N])

    N = int(input())
    graph = [[0 for i in range(N)] for i in range(N)]

    for i in range(N):
        m = list(map(int, input().split()))
        for j in range(N):
            graph[i][j] = m[j]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1

    for q in graph:
        print(*q)
if __name__ == "__main__":
    main()