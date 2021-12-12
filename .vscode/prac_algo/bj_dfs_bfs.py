import sys

def dfs(matrix, V, N):
    visit = []
    stack = []
    stack.append(V)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            i = N
            while(i != 0):
                if(matrix[node][i] == 1):
                    stack.append(i)
                i -= 1

    return visit

def bfs(matrix, V, N):
    visit = []
    queue = []
    queue.append(V)

    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            for i in range(N+1):
                if(matrix[node][i]):
                    queue.append(i)

    return visit
def main():
    N, M, V = map(int, sys.stdin.readline().split())
    matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(M):
        x, y = map(int, sys.stdin.readline().split())
        matrix[x][y] = 1
        matrix[y][x] = 1

    print(*dfs(matrix, V, N))
    print(*bfs(matrix, V, N))

if __name__ == '__main__':
    main()