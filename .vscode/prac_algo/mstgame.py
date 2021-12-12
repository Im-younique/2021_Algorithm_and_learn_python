import sys
import copy

def gamestart(matrix, weight, K, N):
    cut = dict()
    ZF = 0

    for _ in range(K):
        temp = copy.deepcopy(matrix)
        for i in range(len(weight), 0, -1):
            a = weight[i][0]
            b = weight[i][1]
            temp[a][b] = temp[b][a] = 0
            if isST(temp, N):               #mst면 그대로 잘라둠
                cut[i] = [a, b]
                ZF = 1
                continue
            else:
                temp[a][b] = temp[b][a] = 1 #mst가 안되면 다시 붙임

        if(ZF):
            sum = 0
            for j in range(1, len(weight)):
                if j in cut:
                    if(weight[j] == cut[j]):
                        continue
                else:
                    sum += j
            print(sum)
        else:
            print(0)
        
        for i in range(1, len(weight)):  
            a = weight[i][0]
            b = weight[i][1]

            if temp[a][b] == 1:
                temp[a][b] = temp[b][a] = 0
                break 

        matrix = copy.deepcopy(temp)
        ZF=0
        cut.clear()
        
        

def isST(temp, N):
    visited = []
    stack = []

    stack.append(1)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            for k in range(N+1):
                if temp[node][k] == 1:
                    stack.append(k)

    if len(visited) == N:
        return True
    else:
        return False
    

def main():
    N, M, K = map(int, sys.stdin.readline().split())
    matrix = [[0]*(N+1) for i in range(N+1)]
    weight = dict()
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        matrix[a][b] = matrix[b][a] = 1
        weight[i+1] = [a, b]
    gamestart(matrix, weight, K, N)
    
if __name__ == "__main__":
    main()
