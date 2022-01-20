import sys

def dfs(graph, N, start, delete):
    stack = []
    visit = [False for _ in range(N)]
    stack.append(start)
    leaf = 0

    while stack:
        node = stack.pop()
        if visit[node] == False:
            if len(graph[node]) == 0 and node != delete:
                leaf += 1 
            visit[node] = True
            for g in graph[node]:
                stack.append(g)
    
    return leaf

def main():
    N = int(input())
    graph = [[] for _ in range(N)]
    temp = list(map(int, sys.stdin.readline().split()))
    start = 0
    for i in range(len(temp)):
        if temp[i] == -1:
            start = i
            continue
        graph[temp[i]].append(i)
    delete = int(input())

    graph[delete] = []
    for i in range(len(graph)):
        if delete in graph[i]:
            graph[i].remove(delete)

    print(dfs(graph, N, start, delete))

if __name__ == '__main__':
    main()