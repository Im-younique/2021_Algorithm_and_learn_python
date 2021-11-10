parent = {}
rank = {}

def make_set(v):    #초기화
    parent[v] = v
    rank[v] = 0

def find(v):        #대표 노드를 선택
    if parent[v] != v:
        parent[v] = find(parent[v])     #재귀사용
    return parent[v]

def union(u, v):    #합집합
    root1 = find(u)
    root2 = find(v)

    if root1 != root2:
        if rank[root1] > rank[root2]:           #높이가 다를때
            parent[root2] = root1
        else:                                   #높이가 같을때
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1

def kruskal(vertex_list, edge_list):
    for u in vertex_list:                       #각 노드 초기화
        make_set(u)

    edges = edge_list
    edges.sort()
    mst = []
    sum = 0

    for e in edges:
        cost, u, v = e[0], e[1], e[2]           #인접 노드와 cost
        if find(u) != find(v):
            union(u, v)
            mst.append(e)
            sum += cost
    return sum

def main():
    N, M = map(int, input().split())

    vertices = list(map(str, input().split()))     #노드
    edges = []          #링크

    for i in range(1, N+1):
        vertices.append(str(i))
    for _ in range(M):
        u, v, c = map(str, input().split())
        edges.append((int(c), u, v))

    print(kruskal(vertices, edges))

if __name__ == "__main__":
    main()