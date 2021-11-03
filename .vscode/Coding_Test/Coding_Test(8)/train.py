def dfs(matrix, start, n, subway_name):
    stack = []
    visit = []

    stack.append(start)
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            #시작 노드부터 간선이 연결되어있는 기차역 모두 stack에 push
            for k in range(len(matrix[subway_name.index(node)])):
                if matrix[subway_name.index(node)][k] == 1:
                    stack.append(subway_name[k])
    
    if len(visit) == n:
        return True
    else:
        return False

def main():
    n, m = map(int, input().split())    #n은 기차역 수, m은 간선 수
    subway_name = list(map(str, input().split()))   #기차역 리스트
    matrix = [[0]*n for _ in range(n)]      #간선 리스트 초기화

    idx_1 = 0
    idx_2 = 0
    for i in range(m):
        a, b = map(str, input().split())
        for j in range(len(subway_name)):
            if subway_name[j] == a:     #입력값과 기차역 리스트를 비교해서 index
                idx_1 = j
            elif subway_name[j] == b:
                idx_2 = j
        matrix[idx_1][idx_2] = matrix[idx_2][idx_1] = 1 #역과 역사이 간선연결

    print(dfs(matrix, subway_name[0], n, subway_name))

if __name__ == "__main__":
    main()