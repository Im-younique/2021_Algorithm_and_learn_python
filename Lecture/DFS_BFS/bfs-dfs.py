def bfs(graph, start_node):     #큐
    visit = list()
    queue = list()

    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(set(graph[node]) - set(visit))     #방문하지 않은 노드들만 찾는것
            #set으로 하여 자료형의 중복을 제거한다.(필터)

    return visit

def dfs(graph, start_node):     #stack or recursion
    visit = list()
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(set(graph[node]) - set(visit))

    return visit

def dfs_recursive(graph, start, visit=None):
    if visit is None:
        visit = list()

    visit.append(start)

    for next in graph[start]:
        if next not in visit:
            dfs_recursive(graph, next, visit)

    return visit

def main():
    graph = {'A': ['B', 'C'],
            'B' : ['A', 'D', 'E'],
            'C' : ['A', 'F'],
            'D' : ['B'],
            'E' : ['B', 'F'],
            'F' : ['C', 'E']}

    test_bfs = bfs(graph, 'A')
    test_dfs = dfs(graph, 'A')
    test_dfs_re = dfs_recursive(graph, 'A')

    print(test_bfs)
    print(test_dfs)
    print(test_dfs_re)

if __name__ == "__main__":
    main()