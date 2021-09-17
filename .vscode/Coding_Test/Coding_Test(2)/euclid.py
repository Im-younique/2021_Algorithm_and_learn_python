def euclid(a ,b) :
    if b > a :          #a가 b보다 항상 큰 값이 들어갈 순 없으므로 초기화
        a, b = b, a
    if b == 0 :         #재귀를 돌다 b가 0이되면 종료
        return a
    else :
        return euclid(b, a%b)       #유클리드 호제법에 의한 점화식

a, b = map(int, input().split())
print(euclid(a, b))