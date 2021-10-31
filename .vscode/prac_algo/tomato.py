import copy

def dfs(matrix, x, y, n, m):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < n and 0 <= ny and ny < m:
            if matrix[nx][ny] == 0:
                matrix[nx][ny] = 1
    
    return matrix

    

def can(matrix, x, y, n, m):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    cant = False
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < n and 0 <= ny and ny < m:
            if matrix[nx][ny] == 1 | matrix[nx][ny] == 0:
                cant = True

    return cant

def main():
    m, n = map(int, input().split())
    matrix = []
    for _ in range(n):
        my_input = list(map(int, input().split()))
        matrix.append(my_input)
    count = 0
    cant = True
    temp = list()
    while cant:
        if 0 not in matrix:
            temp = copy.deepcopy(matrix)
            for i in range(n):
                for j in range(m):
                    if matrix[i][j] == 1:
                        temp = dfs(temp, i, j, n, m)
                    elif matrix[i][j] == 0:
                        if can(matrix, i, j, n, m) == False:
                            count = -1
                            cant = False
            count += 1
        else:
            break
        matrix = copy.deepcopy(temp)
        
    
    print(count)
                
    

if __name__ == '__main__':
    main()