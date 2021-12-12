import sys

def dfs(matrix, V):
    visit = []
    stack = [1]

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            for i in range(V+1):
                if matrix[node][i] == 1:
                    stack.append(i)
    visit.remove(1)

    return len(visit)
    
def main():
    V = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    matrix = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for i in range(M):
        x, y = map(int, sys.stdin.readline().split())
        matrix[x][y] = 1
        matrix[y][x] = 1

    print(dfs(matrix, V))

if __name__ == '__main__':
    main()