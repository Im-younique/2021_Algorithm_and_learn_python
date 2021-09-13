
def fibonacci(n):
    if n < 2:
        return n       

    #이전의 계산된 값을 저장함으로써 시간을 줄인다.
    cache = [0 for _ in range(n+1)]    #cache 배열을 n+1까지 0으로 초기화한다.
    cache[1] = 1                       
    for i in range(2, n+1) :           #배열에 저장시켜 기억해둬서 시간을 줄임
        cache[i] = cache[i-1] + cache[i-2]  #피보나치 점화식
    return cache[n]


def main():
    n = int(input())
    print(fibonacci(n))

if __name__ == "__main__":
    main()