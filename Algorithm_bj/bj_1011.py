import sys

def main():
    T = int(input())
    res = []
    cntFlag = False
    for _ in range(T):
        cnt = 0
        move = 0
        x, y = map(int, sys.stdin.readline().split())
        distance = y - x
        while move < distance:
            cnt += 1
            if cntFlag:
                move += 1
                cntFlag = True
            else:
                move += 2
                cntFlag = False
        res.append(cnt)
        # 1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7
        # 위의 규칙대로 만들어야함.
    for r in res:
        print(r)

if __name__ == '__main__':
    main()