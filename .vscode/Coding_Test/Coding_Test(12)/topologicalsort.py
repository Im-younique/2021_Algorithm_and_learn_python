#방향성 / 사이클 x 
from collections import defaultdict
import heapq

def main():
    N, M = map(int, input().split())
    alpha = list(map(str, input().split()))
    edges = defaultdict(lambda: [])
    inDegree = defaultdict(lambda: 0)
    for i in range(M):                      #핵심. edges의 value값은 inDegree수치가 올라감
        x, y = map(str, input().split())
        edges[x].append(y)
        inDegree[y] += 1

    queue = []
    result = []

    for i in edges:
        if inDegree[i] == 0:            #inDegree = 0이면 선행하는 값이 없다는 뜻
            heapq.heappush(queue, i)    #최소 힙으로 구현
    
    while queue:
        node = heapq.heappop(queue)     #최소 힙에 의한 pop
        result.append(node)
        for i in edges[node]:           
            inDegree[i] -= 1            #간선이 끊어졌으므로 -1을 해줌.
            if inDegree[i] == 0:        
                queue.append(i)         #순서대로 heap에 넣기위해 그냥 append사용
    
    print(*result)

if __name__ == '__main__':
    main()