import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    distance = int(input())
    allNode = list(sys.stdin.readline().split())
    INF = float('inf')
    edges = [[INF for _ in range(N+1)] for i in range(N+1)]     #edges 초기화
    for i in range(M):
        x, y, z = sys.stdin.readline().split()
        x = allNode.index(x) + 1        #Node마다 index번호 부여됨.
        y = allNode.index(y) + 1
        z = int(z)
        edges[x][y] = z
        edges[y][x] = z                 #양방향 그래프
    for i in range(N):
        edges[i+1][i+1] = 0             #본인으로 가는것 비용 0

    for k in range(1, N+1):             #플로이드 알고리즘 (최소경로 탐색)
        for i in range(1, N+1):
            for j in range(1, N+1):
                if edges[i][j] > edges[i][k] + edges[k][j]:
                    edges[i][j] = edges[i][k] + edges[k][j]
    count = 0
    result_n = ""
    result_c = 0
    for v in range(1, len(allNode)+1):  #distance보다 거리가 짧은 출발지부터 (목적지)까지 찾기.
        count = 0
        for u in range(1, N+1):
            if(distance >= edges[v][u]): #distance보다 짧은 비용이면 count 증가
                count += 1
        if(result_c < count):            #최대값인 노드 및 갯수 저장
            result_n = allNode[v-1]
            result_c = count
    
    print(result_n, result_c)

    
if __name__ == '__main__':
    main()