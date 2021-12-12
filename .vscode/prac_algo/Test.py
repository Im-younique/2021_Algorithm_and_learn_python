import sys, copy

def main():
    N, E = map(int, sys.stdin.readline().split())
    distance = int(sys.stdin.readline())
    Node_list = list(sys.stdin.readline().split())
    INF = float("inf")
    edges = [[INF for _ in range(N+1)] for _ in range(N+1)]

    for i in range(E):
        x, y, c = sys.stdin.readline().split()
        x = Node_list.index(x) + 1
        y = Node_list.index(y) + 1
        c = int(c)
        edges[x][y] = c
        edges[y][x] = c
    
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if edges[i][j] > edges[i][k] + edges[k][j]:
                    edges[i][j] = edges[i][k] + edges[k][j]
    
    max = 0
    res_node = ''
    for i in range(1, N+1):
        count = 0
        for j in range(1, N+1):
            if distance >= edges[i][j]:
                count += 1
        if max < count:
            max = count
            res_node = Node_list[i-1]

    print(res_node, max)

if __name__ == '__main__':
    main()