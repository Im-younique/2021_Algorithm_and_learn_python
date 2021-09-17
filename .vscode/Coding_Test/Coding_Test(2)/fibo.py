def fibo(n):
    if n <= 1 :         #n이 1보다 작거나 같으면 n값을 출력 (피보나치 초기 값)
        return n
    return fibo(n-1) + fibo(n-2)       #피보나치 수열 점화식

n = int(input())
print(fibo(n))