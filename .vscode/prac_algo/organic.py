import sys

def find(matrix, x, y, M, N):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]  #동 서 북 남
    for i in range(4):
        rx = x + dx[i]
        ry = y + dy[i]
        if rx >= 0 and rx < N and ry >= 0 and ry < M:
            if matrix[rx][ry] == 1:
                matrix[rx][ry] = 0
                find(matrix, rx, ry, M, N)
    
    return

def dfs(matrix, M, N):
    cnt = 0

    for i in range(N):
        for j in range(M):
            if(matrix[i][j] == 1):
                cnt += 1
                matrix[i][j] = 0
                find(matrix, i, j, M, N)
    
    return cnt


def main():
    sys.setrecursionlimit(100000)           #재귀 깊이한도 설정. 기본 1000
    T = int(sys.stdin.readline())
    result = []
    for i in range(T):
        M, N, K = map(int, sys.stdin.readline().split())
        matrix = [[0 for _ in range(M)] for _ in range(N)]
        for _ in range(K):
            x, y = map(int, sys.stdin.readline().split())
            matrix[y][x] = 1
        result.append(dfs(matrix, M, N))
    
    for i in range(len(result)):
        print(result[i])

if __name__ == '__main__':
    main()