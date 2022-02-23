import sys

def main():
    T = int(input())
    for _ in range(T):
        vps = sys.stdin.readline()
        vps = list(vps)
        vps.pop()
        temp = []
        for _ in range(len(vps)):
            now = vps.pop(0)
            if len(temp) == 0:
                temp.append(now)
            else:
                if now == '(':
                    temp.append(now)
                elif now == ')':
                    if temp[len(temp)-1] == '(':
                        temp.pop()
                    else:
                        temp.append(now)
        
        if len(temp) == 0:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()