#1개 또는 2개 계단을 오를 수 있을 때, n개 계단을 올라야할 때 경우의 수


def stair(n):           #큰 수가 들어가면 시간초과.. 중복제어 연습
    if n <= 1:
        return 1
    elif n == 2:
        return stair(1) + stair(0)
    else:
        return stair(n-1) + stair(n-2)

def main():
    n = int(input())

    print(stair(n))

if __name__ == '__main__':
    main()