import copy

def dfs(matrix, start_node, N):  #dfs 구현
    visit = list()
    stack = list()
    
    stack.append(start_node)
    
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            for j in range(len(matrix[node])):      #간선에 연결되어 있는 곳을 stack에 넣는다
                if matrix[node][j] == 1:
                    stack.append(j) 

    for i in range(N):      #edge 갯수 만큼(모든 곳은 순회 했는지)  
        if i in visit:
            continue
        else:               #start_node로 부터 모든 도시 방문이 안되면 false
            return False
    return True        

def main():
    N, M = map(int, input().split())    
    # N : 정점(edge)의 개수 / M : 간선의 갯수
    matrix = [[0]*(N) for i in range(N)]    #graph를 모두 0으로 채운다.    [0]과 연결되어있는 간선 / [1]과 연결된 간선 [2]와 연결된 간선 [3] --- 모두 0으로 초기화
    al = list()
    bl = list()
    result = list()
    for i in range(M):
        a, b = map(int, input().split())    #input 값 처리
        al.append(a)
        bl.append(b)
        matrix[al[i]][bl[i]] = matrix[bl[i]][al[i]] = 1     #2개씩 들어오는 input은 간선으로 연결되어 있음 표시 1
    #기본 matrix 완성
    #matrix는 간선이 연결되어 있는걸 표시해주고 있다.
    for i in range(M):
        temp = copy.deepcopy(matrix)                    #deep copy로 초기화
        temp[al[i]][bl[i]] = temp[bl[i]][al[i]] = 0     #해당 간선을 끊는다.
        for j in range(N):                              #시작 노드를 모든 도시로 부터 시작해서 한개라도 끊기면 false
            if dfs(temp, j, N):
                continue
            else:
                result.append([al[i], bl[i]])
                break
    
    result.sort()
    for i in range(len(result)):
        print(*result[i])

if __name__ == '__main__':
    main()
