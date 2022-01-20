import sys

def union(graph):
    dep1 = []
    cnt = 0

    for i in range(len(graph[1])):
        if graph[1][i] == 1:
            dep1.append(i)
    
    dep1.append(1)

    dep2 = set()
    
    for s in dep1:
        for i in range(len(graph[s])):
            if graph[s][i] == 1 and i not in dep1:
                dep2.add(i)
                
    res = len(dep1) - 1 + len(dep2)
    return res


def main():
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a][b] = graph[b][a] = 1

    print(union(graph))


if __name__ == '__main__':
    main()