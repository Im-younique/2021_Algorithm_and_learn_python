import sys
sys.setrecursionlimit(10**6)    #재귀최대횟수 10의 6승

def fibonacci(n):           #중복된 계산이 많이 된다.(값이 커지면 계산시간 급증)
    if n <= 1:              #재귀함수 종료조건  
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def main():
    n = int(input())
    print(fibonacci(n))

if __name__ == "__main__":
    main()