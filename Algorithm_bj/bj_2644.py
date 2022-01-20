import sys

def dfs(d1, matrix, cnt):
    for i in matrix[d1]:
        if cnt[i] == 0:
            cnt[i] = cnt[d1] + 1
            dfs(i, matrix, cnt)

def main():
    N = int(sys.stdin.readline())
    d1, d2 = map(int, sys.stdin.readline().split())
    M = int(sys.stdin.readline())
    matrix = [[] for _ in range(N+1)]
    for _ in range(M):
        p, c = map(int, sys.stdin.readline().split())
        matrix[p].append(c)
        matrix[c].append(p)
    
    cnt = [0]*(N+1)
    dfs(d1, matrix, cnt)
    
    if cnt[d2] > 0:
        print(cnt[d2])
    else:
        print(-1)

if __name__ == '__main__':
    main()