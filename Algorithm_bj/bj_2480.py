import sys

def main():
    t1, t2, t3 = map(int, sys.stdin.readline().split())

    if t1 == t2 == t3:
        print(10000 + t1*1000)
    elif t1 == t2 or t1 == t3:
        print(1000 + t1*100)
    elif t2 == t3:
        print(1000 + t2 *100)
    else:
        temp = [t1, t2, t3]
        num = max(temp)
        print(num*100)
    
if __name__ == '__main__':
    main()