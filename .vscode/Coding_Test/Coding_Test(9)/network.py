import sys
import heapq

def prim(edges, N):     
    queue = []
    #비용, 현재노드, 다음노드
    heapq.heappush(queue, [0, 0, 1])            #임의의 노드

    visit = [ False for _ in range(N+1)]
    sum = 0
    
    while queue:
        h = heapq.heappop(queue)                #최소 힙 빼내기
        if visit[h[2]] == True:                 #방문했으면 pass
            continue
        else:
            visit[h[2]] = True
            sum += h[0]
    
        for e in edges[h[2]]:
            if (visit[e[0]]):
                continue
            heapq.heappush(queue, [e[1], h[2], e[0]])   #비용, 현재노드, 다음노드 순서!
    
    return sum

def main():
    N, M = map(int, sys.stdin.readline().split())
    bulid_cost = list(map(int, sys.stdin.readline().split()))

    bulid_cost.insert(0, 0)                             #index에 임의로 0추가
    edges = [ [] for _ in range(N+1)]
    for _ in range(M):
        u, v, c = map(int, sys.stdin.readline().split())
        edges[u].append([v, c])
        edges[v].append([u, c])
    
    for i in range(1, len(bulid_cost)):         #hint! 임의의 노드와 자기를 연결하는 건설간선 만듦.
        edges[0].append([i, bulid_cost[i]])     #그것을 edges빈공간인 0에 넣었다.
        edges[i].append([0, bulid_cost[i]])
        
    print(prim(edges, N))

    
if __name__ == '__main__':
    main()