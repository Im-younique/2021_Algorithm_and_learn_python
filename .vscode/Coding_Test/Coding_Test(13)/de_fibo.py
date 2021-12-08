import sys

def fibo(a):
    fibo_list = [0]
    for i in range(1, a+1):
        if i <= 2:
            fibo_list.append(1)
        else:
            fibo_list.append(fibo_list[i-1] + fibo_list[i-2])
    
    return fibo_list[a]

def main():
    N = int(sys.stdin.readline())
    print(fibo(N))
if __name__ == '__main__':
    main()