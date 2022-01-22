import sys

def main():
    N = int(input())
    dot = []
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        dot.append([x, y])
    
    dot.sort(key=lambda x : (x[1], x[0]))

    for d in dot:
        print(*d)

if __name__ == '__main__':
    main()