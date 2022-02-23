import sys

def main():
    N = int(input())
    temp = []
    for _ in range(N):
        my_cmd = sys.stdin.readline().strip()
        if my_cmd == "top":
            if len(temp) == 0:
                print(-1)
            else:
                print(temp[len(temp)-1])
        elif my_cmd == "empty":
            if len(temp) == 0:
                print(1)
            else:
                print(0)
        elif my_cmd == "size":
            print(len(temp))
        elif my_cmd == "pop":
            if len(temp) == 0:
                print(-1)
            else:
                p = temp.pop()
                print(p)
        else:
            my_str, num = my_cmd.split()
            temp.append(num)

if __name__ == '__main__':
    main()