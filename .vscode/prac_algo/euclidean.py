# 유클리드 호제법
# 2개의 자연수 또는 정식의 최대공약수를 구하는 알고리즘


def euclid(a, b) :
    # if(b > a) :
    #     euclid(b, a)
    if b == 0 :
        return a
    else :
        return euclid(b, a%b)

a, b = map(int, input().split())        #동시에 변수 입력받음
print(euclid(a, b))