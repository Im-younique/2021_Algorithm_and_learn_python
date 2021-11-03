
def main():
    base = list(map(int, input().split()))
    elec = list(map(int, input().split()))

    leftmin = 10000000      #엄청 큰 수로 최소값 초기화
    rightmin = 10000000
    min_list = []
    for b in base:
        for e in elec:
            #왼쪽에 전력공급이 있는경우
            if e < b:
                if leftmin > b-e:
                    leftmin = b-e
            #오른쪽에 전력공급이 있는경우
            else:
                if rightmin > e-b:
                    rightmin = e-b
        if leftmin < rightmin:      #전력공급 최소값 리스트 만들기
            min_list.append(leftmin)
        else:
            min_list.append(rightmin)   
        leftmin = 10000000
        rightmin = 10000000        #초기화

    min_list.sort()
    print(min_list[len(min_list)-1])    #소팅된 최소값 리스트중 가장 큰 값 출력

if __name__ == '__main__':
    main()