import sys

def main():
    M, N = map(int, sys.stdin.readline().split())
    matrix = [[0 for _ in range(N)] for _ in range(M)]
    for _ in range(M):
        matrix[_] = list(sys.stdin.readline().split())

    #let's brute

if __name__ == '__main__':
    main()