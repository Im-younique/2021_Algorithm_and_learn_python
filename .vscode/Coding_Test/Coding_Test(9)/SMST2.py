import copy
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
        cost, u, v = e[0], e[1], e[2]
        if find(u) != find(v):
            union(u, v)
            mst.append(e)
            sum += cost
    return sum

def main():
    N, M = map(int, input().split())

    vertices = list(map(str, input().split()))     #노드
    edges = []          #링크
    sum_list = set()

    for i in range(1, N+1):
        vertices.append(str(i))
    for _ in range(M):
        u, v, c = map(str, input().split())
        edges.append((int(c), u, v))

    for k in range(M):                           #각 간선 하나씩 빼보고 kruskal 돌려봄
        temp = copy.deepcopy(edges)
        temp.pop(k)
        sum_list.add(kruskal(vertices, temp))   #sum_list에 set형태로 중복없이 넣음
    
    sum_list = list(sum_list)           #list형태로 변환
    sum_list.sort()                     
    print(sum_list[1])                  #소팅되면 두번째 인덱스인 1에 최소보다 하나 높은 값이 있음.


if __name__ == "__main__":
    main()