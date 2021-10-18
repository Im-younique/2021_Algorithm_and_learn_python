# 정사각형 모양의 지도가 있다. 1은 집이 있는 곳, 0은 집이 없는 곳을 나타낸다.
# 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙인다.
# 대각선상의 집이 있는 경우는 연결된 것이 아니다.
# 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하라.

# 첫 번째 줄에는 지도의 크기 (5<=N<=25) 그 다음 N줄에는 N개의 자료(0|1) 입력된다.

# 첫 번째 줄에는 총 단지수, 각 단지내 집의 수를 오름차순으로 정렬하여 한줄에 하나씩 출력하라.

def dfs(matrix, n, count, x, y):
    matrix[x][y] = 0    #방문을 하면 0으로 바꾼다.
    dx = [1, -1, 0, 0]
    dy = [0, 0 , 1, -1] #동서남북(방향)

    for i in range(4):  #네 방향에 대해서 처리한다.
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if matrix[nx][ny] == 1:
                count = dfs(matrix, n, count+1, nx, ny)     #재귀하여 단지 찾기.

    return count


def main():
    n = int(input())                #입력개수
    matrix = [list(map(int, input())) for _ in range(n)]    #맵

    apartment_block = []        #단지 블럭(단지 개수)
    for i in range(n):
        for j in range(n):      #모든 행렬값을 다 읽는다.
            if matrix[i][j] == 1:   # 1이 된 값만 처리한다.
                apartment_block.append(dfs(matrix, n, 1, i, j))     #시작점 i,j pointer

    print(len(apartment_block))
    for i in sorted(apartment_block):
        print(i)

if __name__ == "__main__":
    main()