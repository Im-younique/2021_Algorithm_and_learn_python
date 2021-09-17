#n,m 
#n은 오르고자하는 계단 최대 수(destination)
#m은 한번에 오를 수 있는 최대 수(hulk_step)


def hulk_stair(n, m): 
    if n <= m :                 #n < m 보다 크거나 같으면 2 ** (n - 1) 이 성립한다.
        return 2**(n-1)         #total에 값을 넣어주는 식

    total = 0
    for x in range(1,m+1):              #x는 1부터 m까지
        total += hulk_stair(n-x, m)     #n즉 목적지를 줄여가면서 재귀실행 
                                        #cuz 목적지 전의 칸수에 경우의 수를 추가되서 합해진다.
    return total

n, m = map(int, input().split())

print (hulk_stair(n,m))
