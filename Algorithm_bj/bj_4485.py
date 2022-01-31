import sys, heapq

def dij(N, edges):
    INF = float('inf')
    distance = [[INF for _ in range(N)] for _ in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    distance[0][0] = edges[0][0]

    queue = []
    heapq.heappush(queue, [5, 0, 0])    #비용, x좌표, y좌표

    while queue:
        mc, mx, my = heapq.heappop(queue)
        for i in range(4):
            if 0 <= mx + dx[i] < N and 0 <= my + dy[i] < N:   #간선연결된 곳
                if distance[mx+dx[i]][my+dy[i]] > distance[mx][my] + edges[mx+dx[i]][my+dy[i]]:
                    distance[mx+dx[i]][my+dy[i]] = distance[mx][my] + edges[mx+dx[i]][my+dy[i]]     #갱신
                    heapq.heappush(queue, [distance[mx+dx[i]][my+dy[i]], mx+dx[i], my+dy[i]])
    
    return distance[N-1][N-1]


def main():
    res = []
    while True:
        N = int(input())
        if N == 0:
            break
        edges = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            edges[i] = list(map(int, sys.stdin.readline().split()))
        
        res.append(dij(N, edges))
    
    for r in range(len(res)):
        print("Problem {0}: {1}".format(r+1, res[r]))

if __name__ == '__main__':
    main()