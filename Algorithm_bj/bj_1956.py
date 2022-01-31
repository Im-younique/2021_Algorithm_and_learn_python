import sys

def main():
    V, E = map(int, sys.stdin.readline().split())
    INF = float('inf')
    edges = [[INF for _ in range(V+1)] for _ in range(V+1)]
    for _ in range(E):
        a, b, c = map(int, sys.stdin.readline().split())
        edges[a][b] = c

    result = INF
    for k in range(1, V+1):                 #플로이드 와셜
        for i in range(1, V+1):
            for j in range(1, V+1):
                if edges[i][j] > edges[i][k] + edges[k][j]:
                    edges[i][j] = edges[i][k] + edges[k][j]

    for i in range(1, V+1):
        result = min(result, edges[i][i])
    
    if result == INF:
        print(-1)
    else:
        print(result)

if __name__ == '__main__':
    main()