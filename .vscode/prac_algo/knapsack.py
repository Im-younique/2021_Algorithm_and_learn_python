import sys

def knaspack(N, K, w_arr, v_arr):   #갯수, 최대무게, 무게배열, 가치배열
    row_col = [[0 for _ in range(K+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, K+1):         #j는 현재 최대무게 제한값이 된다.
            if(w_arr[i] <= j) :        #현재 들어가려는 물건의 무게가 현재 최대무게 보다 작은경우
                row_col[i][j] = max(v_arr[i]+row_col[i-1][j-w_arr[i]], row_col[i-1][j])
                # 현재밸류 + 이전까지 합산해온 최대밸류와 / 매트릭스 기준 위에있는 값. (현재 최대무게의 최대값)
            else:
                row_col[i][j] = row_col[i-1][j]     #그냥 저장된 값 가져옴
    return row_col[N][K]
                

def main():
    N, K = map(int, sys.stdin.readline().split())     #갯수, 최대무게
    w_arr = [0]
    v_arr = [0]
    for _ in range(N):
        k, v = map(int, sys.stdin.readline().split())
        w_arr.append(k)
        v_arr.append(v)
    print(knaspack(N, K, w_arr, v_arr))


if __name__ == "__main__":
    main()