
def stair(n):
    if n <= 1:
        return n
    dp = [int(0) for _ in range(n+1)]     #초기값
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return(dp[n])

def main():
    n = int(input())
    print(stair(n))

if __name__ == '__main__':
    main()