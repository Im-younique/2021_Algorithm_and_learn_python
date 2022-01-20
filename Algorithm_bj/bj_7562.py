import sys

def bfs(matrix, x, y, dx, dy, lenn):
    mx = [1, 2, 2, 1, -1, -2, -2, -1]
    my = [2, 1, -1, -2, -2, -1, 1, 2]
    queue = []
    queue.append((x, y))

    while queue:
        nowX, nowY = queue.pop(0)
        if nowX == dx and nowY == dy:
            return matrix[dx][dy] -1
        
        for i in range(8):
            tx = nowX + mx[i]
            ty = nowY + my[i]
            if tx < 0 or tx > lenn-1 or ty < 0 or ty > lenn-1:
                continue
            elif matrix[tx][ty] == 0:
                matrix[tx][ty] = matrix[nowX][nowY] + 1
                queue.append((tx, ty))
    
def main():
    res = []
    T = int(sys.stdin.readline())
    for _ in range(T):
        lenn = int(sys.stdin.readline())
        matrix = [[0]*(lenn+1) for _ in range(lenn+1)]
        nx, ny = map(int, sys.stdin.readline().split())
        dx, dy = map(int, sys.stdin.readline().split())
        matrix[nx][ny] = 1
        res.append(bfs(matrix, nx, ny, dx, dy, lenn))
    
    for r in res:
        print(r)

if __name__ == '__main__':
    main()