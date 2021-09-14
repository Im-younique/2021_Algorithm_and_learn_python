#피보나치 수열 
#조건 n >= 1

def fibo_recursion(n):                #중복계산이 많아진다.
    if n <= 2:
        return 1
    else:
        return fibo_recursion(n-1) + fibo_recursion(n-2)


def fibo_time(n):                   #리스트에 기억시켜 시간단축
    if(n <= 2) :
        return 1
    
    list = []
    list = [0 for _ in range(0, n+1)]
    list[1] = 1
    list[2] = 1
    for i in range(2, n+1):
        list[i] = list[i-1] + list[i-2]

    return list[n]
        


n = int(input())
print(fibo_recursion(n))
print(fibo_time(n))