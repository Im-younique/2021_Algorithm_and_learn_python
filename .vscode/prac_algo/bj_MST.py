import sys,heapq

def prim(matrix):
    visit = []
    queue = []
    result = 0
    heapq.heappush(queue, [0, 0, 1])    #cost, now, next

    while queue:
        cost, now, next = heapq.heappop(queue)
        if next not in visit:
            visit.append(next)
            result += cost
            for j in matrix[next]:
                heapq.heappush(queue, [j[1], next, j[0]])

    return result

def main():
    V, E = map(int, sys.stdin.readline().split())
    matrix = [[] for _ in range(V+1)]
    for i in range(E):
        s, d, c = map(int, sys.stdin.readline().split())
        matrix[s].append([d, c])
        matrix[d].append([s, c])
    
    print(prim(matrix))

if __name__ == '__main__':
    main()