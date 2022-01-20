import sys, math

def main():
    T = int(input())
    for _ in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
        d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2) #두원의 중심좌표간의 거리

        if d == 0:
            if r1 == r2:
                print(-1)
            else:
                print(0)
        else:
            if r1 + r2 == d or abs(r1 - r2) == d:
                print(1)
            elif abs(r1 - r2) < d < r1+r2:
                print(2)
            else:
                print(0)

if __name__ == '__main__':
    main()