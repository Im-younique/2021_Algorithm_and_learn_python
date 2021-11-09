from math import log2
from collections import deque

def generate_tree(tree, N):
    for _ in range(N - 1):
        parent, child = map(int, input().split())   #N-1개의 간선
        tree[child].append(parent)          #간선연결
        tree[parent].append(child)

def dfs(tree, parent_list, depth, N):
    visited = [False for _ in range(N+1)]
    q = deque()     #큐(사실은 스택임)
    q.append(1)

    while q:        #노드 순회(DFS(preorder))
        p = q.popleft()
        visited[p] = True
        for i in tree[p]:
            if visited[i] == False:
                q.append(i)
                parent_list[i] = p
                depth[i] = depth[p] + 1     #노드의 depth계산

def compute_exp_parent(exp_parent, N):
    logN = int(log2(N) + 1)
    for i in range(1, N+1):
        for j in range(1, logN):    #로그 값이 인덱스로 들어감
            exp_parent[i][j] = exp_parent[exp_parent[i][j-1]][j-1]
            #2^i = 2^i-1 + 2^i-1

def search_lca(exp_parent, depth, N, M):
    logN = (int)(log2(N) + 1)
    for _ in range(M):
        a, b = map(int, input().split())        #테스트케이스
        if depth[a] > depth[b]:         #depth가 다르면 한쪽으로 맞춰줌
            a, b = b, a
        level_diff = depth[b] = depth[a]    #depth 다름의 높이 차이
        for i in range(logN):
            if level_diff & 1 << i:         #몇 칸을 이동하느냐
                b = exp_parent[b][i]        #i만큼 이동..?

        if a == b:      #답이 바로나오는 경우
            print(a)
            continue

        for i in range(logN - 1, -1, -1):   #2^k, 2^k-1 ??
            if exp_parent[a][i] != exp_parent[b][i]:    #다르면 직전 parent를 찾음
                a = exp_parent[a][i]
                b = exp_parent[b][i]

        print(exp_parent[b][0])     #a나 b나 상관없음.

def main():
    N = int(input())            #노드의 갯수
    tree = [[] for _ in range(N + 1)]   
    generate_tree(tree, N)      #트리를 만듬

    parent_list = [0 for _ in range(N+1)]   #트리의 노드들의 parent를 찾기
    depth = [0 for _ in range(N+1)]         #parent를 찾으면서 depth를 계산
    dfs(tree, parent_list, depth, N)

    logN = (int)(log2(N) + 1)               #log2의 N
    exp_parent = [[0 for _ in range(logN)] for i in range(N+1)]     #지수함수의 parent의 list  
    for i in range(N + 1):
        exp_parent[i][0] = parent_list[i]
    compute_exp_parent(exp_parent, N)

    M = int(input())            #테스트 케이스
    search_lca(exp_parent, depth, N, M)