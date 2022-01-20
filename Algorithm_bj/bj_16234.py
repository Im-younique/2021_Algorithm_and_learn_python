import sys

def bfs(matrix, N, L, R):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    myFlag = True
    cnt = 0

    queue = []
    while myFlag:
        for i in range(N):
            for j in range(N):
                group = []
                group.append((i, j))
                for k in range(4):
                    gx = i + dx[k]
                    gy = j + dy[k]
                    if gx < 0 or gx >= N or gy < 0 or gy >= N:
                        continue
                    elif abs(matrix[i][j] - matrix[gx][gy]) >= L and abs(matrix[i][j] - matrix[gx][gy]) <= R:
                        group.append((gx, gy))
                group.sort()
                if len(group) != 1 and group not in queue:
                    queue.append(group) #여기 수정 필요

        if queue:
            cnt += 1
        else:
            myFlag = False
        
        anQueue = []
        res = []
        while queue:
            visit = [[False for _ in range(N)] for _ in range(N)]
            group_li = queue.pop(0)
            while group_li:
                nowX, nowY = group_li.pop(0)
                if visit[nowX][nowY] == True:
                    continue
                visit[nowX][nowY] = True
                res.append(matrix[nowX][nowY])
                anQueue.append((nowX, nowY))
                for i in range(4):
                    tx = nowX + dx[i]
                    ty = nowY + dy[i]
                    if tx < 0 or tx >= N or ty < 0 or ty >= N:
                        continue
                    elif abs(matrix[nowX][nowY] - matrix[tx][ty]) >= L and abs(matrix[nowX][nowY] - matrix[tx][ty]) <= R:
                        visit[tx][ty] = True
                        anQueue.append((tx, ty))
                        res.append(matrix[tx][ty])
            myRes = 0
            for r in range(len(res)):
                myRes += res[r]
            if len(res) == 0:
                continue
            myRes = myRes//len(res)
            while anQueue:
                myX, myY = anQueue.pop(0)
                matrix[myX][myY] = myRes
    
    return cnt


def main():
    N, L, R = map(int, sys.stdin.readline().split())
    #L명이상, R명 이하
    matrix = [[0 for _ in range(N)]for _ in range(N)]

    for i in range(N):
        my_arr = list(map(int, sys.stdin.readline().split()))
        for j in range(len(my_arr)):
            matrix[i][j] = my_arr[j]
    
    print(bfs(matrix, N, L, R))

if __name__ == '__main__':
    main()