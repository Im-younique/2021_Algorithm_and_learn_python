parent = {}
rank = {}

def make_set(v):    #초기화
    parent[v] = v
    rank[v] = 0

def find(v):        #대표 노드를 선택
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(u, v):
    root1 = find(u)
    root2 = find(v)

    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1

def kruskal(vertex_list, edge_list):
    for u in vertex_list:
        make_set(u)

    edges = edge_list
    edges.sort()
    mst = []
    sum = 0

    for e in edges:
        cost, u, v = 0
        if find(u) != find(v):
            union(u, v)
            mst.append(e)
            sum += cost
    return sum, mst

def main():
    N = int(input())
    M = int(input())

    vertices = []       #노드
    edges = []          #링크

    for i in range(1, N+1):
        vertices.append(str(i))
    for _ in range(M):
        u, v, c = map(int, input().split())
        edges.append((c, str(u), str(v)))

    print(kruskal(vertices, edges))

if __name__ == "__main__":
    main()