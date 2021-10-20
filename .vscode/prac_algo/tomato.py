import sys

def dfs(start_node_x, start_node_y):
    visit_map[start_node_x][start_node_y] = 1
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]      #상하좌우 탐색

    for i in range(4):      #네 방향 탐색
        nx = start_node_x + dx[i]
        ny = start_node_y + dy[i]
        if(nx < N and nx >= 0) and (ny < M and ny >= 0):      #index초과 방지
            if matrix[nx][ny] == 0:     #토마토 익어요잇
                visit_map[nx][ny] = 1




M, N = map(int, sys.stdin.readline().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

visit_map = [[0]*M for i in range(N)]       # 0으로만 초기화 된 visit 배열
count = 0
while 0 in visit_map:                 #이거 왜 안먹어요..
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                start_node_idx = i
                start_node_idy = j
                dfs(start_node_idx, start_node_idy)
    #탐색이 끝나면 matrix에 visit map을 넣는다.
    matrix = visit_map
    count += 1

print(count)
