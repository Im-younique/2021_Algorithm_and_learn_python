import sys

def fibo(a):
    fibo_list = [0]                 #피보나치 수열 배열에 하나씩 저장하는 dp사용
    for i in range(1, a+1):
        if i <= 2:
            fibo_list.append(1)
        else:
            fibo_list.append(fibo_list[i-1] + fibo_list[i-2])
    
    return fibo_list[a]             #원하는 위치까지만 구함

def main():
    N = int(sys.stdin.readline())
    print(fibo(N))
if __name__ == '__main__':
    main()