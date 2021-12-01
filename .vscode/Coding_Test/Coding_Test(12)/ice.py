#에이스타
import heapq

def a_star(graph, start, end, weight, row, col):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    distance = [[float('inf') for _ in range(col)] for _ in range(row)]
    distance[start[0]][start[1]] = 0
    queue = []
    found = [[False for _ in range(col)] for _ in range(row)]

    heapq.heappush(queue, [0, start[0], start[1]]) #최초 힙 [거리, x좌표, y좌표]

    while queue:
        node = heapq.heappop(queue)
        found[node[1]][node[2]] = True
        for i in range(4): #동, 서, 남, 북 탐색 (인접노드 방문)
            nx = node[1] + dx[i]
            ny = node[2] + dy[i]
            if nx >= 0 and nx < row and ny >= 0 and ny < col:      #graph index범위 벗어나는것 방지
                if found[nx][ny] == True:
                    continue
                if graph[nx][ny] == 'E':
                    graph[nx][ny] = 0
                if distance[nx][ny] > node[0] + int(graph[nx][ny]):
                    distance[nx][ny] = node[0] + int(graph[nx][ny])
                    heapq.heappush(queue, [distance[nx][ny], nx, ny])

    if weight - distance[end[0]][end[1]] < 0:
        return "FAIL"
    else:
        return weight - distance[end[0]][end[1]]
    

def main():
    row, col, weight = map(int, input().split())
    graph = [[0 for _ in range(col)] for _ in range(row)]
    for i in range(row):
        line =  input()
        for j in range(col):
            graph[i][j] = line[j]
            if line[j] == 'S':
                start_node = [i, j]
            if line[j] == 'E':
                end_node = [i, j]

    # melting weight는 graph[node[0]][node[1]] 즉 capacity
    print(a_star(graph, start_node, end_node, weight, row, col))
                
if __name__ == "__main__":
    main()