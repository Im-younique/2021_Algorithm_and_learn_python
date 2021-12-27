import sys

def knaspack(C, N, wl, vl):
    K = [[0 for _ in range(C+1)] for _ in range(N+1)]     #최종 값 전에 이전값까지 모두 구해서 저장
    for i in range(1, N+1):
        for j in range(1, C+1):             #이전의 matrix에서의 값을 이용해서 구함
            if(wl[i] <= j):
                K[i][j] = max(K[i-1][j], vl[i]+K[i-1][j-wl[i]])     #점화식 기반 풀이
            else:
                K[i][j] = K[i-1][j]
    
    return K[N][C]


def main():
    C = int(sys.stdin.readline())
    N = int(sys.stdin.readline())
    wl = list(map(int, sys.stdin.readline().split()))
    wl.insert(0, 0)     #가로 첫째줄 비우기
    vl = list(map(int, sys.stdin.readline().split()))
    vl.insert(0, 0)     #세로 첫째줄 비우기
    print(knaspack(C, N, wl, vl))

if __name__ == '__main__':
    main()
