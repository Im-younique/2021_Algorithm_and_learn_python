import sys

def main():
    while True:
        myput = sys.stdin.readline().rstrip()
        if myput == '.':
            break
        myput = list(myput)
        temp = []
        for _ in range(len(myput)):
            now = myput.pop(0)
            if now == "(" or now == "[":
                temp.append(now)
            elif now == ")":
                if len(temp) == 0:
                    temp.append(now)
                elif temp[len(temp)-1] == "(":
                    temp.pop()
                else:
                    temp.append(now)
            elif now == "]":
                if len(temp) == 0:
                    temp.append(now)
                elif temp[len(temp)-1] == "[":
                    temp.pop()
                else:
                    temp.append(now)
            else:
                continue
        
        if len(temp) == 0:
            print("yes")
        else:
            print("no")
        

if __name__ == '__main__':
    main()