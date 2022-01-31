
def myP(many, cnt, max, i, num):
    if max < cnt:
        max = cnt
        many.clear()
        many.append(num[i])
    elif max == cnt:
        many.append(num[i])
    cnt = 1
    return max, cnt

def main():
    N = int(input())
    num = []
    res = []
    avr = 0
    for _ in range(N):
        my_in = int(input())
        avr += my_in
        num.append(my_in)
    
    my_len = len(num)
    res.append(round(avr/my_len))       #산술평균
    
    num.sort()
    res.append(num[int(my_len/2)])      #중앙값
    
    many = []                           #최빈값
    cnt = 1
    max = 1
    for i in range(N):
        if i == N-1:
            max, cnt = myP(many, cnt, max, i, num)
        elif num[i] == num[i+1]:
            cnt += 1
        else:
            max, cnt = myP(many, cnt, max, i, num)
    
    many.sort()
    if len(many) == 1:
        res.append(*many)
    else:
        res.append(many[1])
        

    res.append(num[len(num)-1] - num[0])  #범위

    for r in res:
        print(r)

if __name__ == '__main__':
    main()