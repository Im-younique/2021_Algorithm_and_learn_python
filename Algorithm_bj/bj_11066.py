import sys

def mydp(N, numlist):
    result = list()
    while len(numlist) != 1:
        min = float('inf')
        idx = 0
        for i in range(len(numlist)-1):
            temp = numlist[i] + numlist[i+1]
            if min > temp:
                min = temp
                idx = i
        numlist.pop(idx)
        numlist.insert(idx, min)
        numlist.pop(idx+1)
        result.append(min)
    
    res = 0
    for r in result:
        res += r

    return res


def main():
    T = int(input())
    for _ in range(T):
        K = int(input())
        numlist = list(map(int, sys.stdin.readline().split()))
        print(mydp(K, numlist))

if __name__ == '__main__':
    main()