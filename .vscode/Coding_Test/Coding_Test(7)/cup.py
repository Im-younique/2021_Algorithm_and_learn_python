def dfs(graph, start_node, N):  #dfs로 그래프 탐색
    visit = list()
    stack = list()
    
    stack.append(start_node)
    
    while stack:
        node = stack.pop()
        if node not in visit:       #조건에 맞으려면 visit에 마지막 컵(N-1) 값이 방문되야 함
            visit.append(node)
            stack.extend(graph[node])
            
    if N-1 in visit:        #마지막 컵(N-1)에 도달 가능한지 체크
        return True
    else:
        return False

def main():
    N  = int(input())       # 컵의 갯수
    matrix = {}
    for i in range(N):      # i = 0, 1, 2, 3
        line_input = list(map(int, input().split()))     
        matrix[i] = line_input
        
    print(dfs(matrix, 0, N))
    
    
if __name__ == '__main__':
    main()