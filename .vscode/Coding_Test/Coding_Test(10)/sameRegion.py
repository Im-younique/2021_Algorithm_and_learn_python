import sys

def main():
    N = int(input())
    target1, target2 = sys.stdin.readline().split()
    my_dict = {}
    contry = ""
    city = list()
    for i in range(N):
        my_input = list(map(str, sys.stdin.readline().split()))
        if(i == 0):
            my_dict["0"] = my_input[0]
            contry = my_input[0]
            city = list(my_input[1:])
        parent = my_input[0]
        child = my_input[1:]
        my_dict[parent] = child
    
    target1_cnt = 0     #초기화
    target2_cnt = 0     #초기화
    if target1 in contry:
        target1_cnt = 1
    elif target1 in city:
        target1_cnt = 2
    else:
        target1_cnt = 3         #최종 depth는 3이 최대이다.

    if target2 in contry:
        target1_cnt = 1
    elif target2 in city:
        target2_cnt = 2
    else:
        target2_cnt = 3

    while target1 != target2:   #target1과 target2가 같으면 lca값 찾음.
        if(target1_cnt == 0 or target2_cnt == 0):   #공통 부모노드가 없는 경우
            target1 = 0
            break
        if target1_cnt > target2_cnt:       #높이 맞추기
            target1_cnt -= 1
            for k, v in my_dict.items():
                if target1 in v:
                    target1 = k
                    break
        elif target2_cnt < target2_cnt:     #높이 맞추기
            target2_cnt -= 1
            for k, v in my_dict.items():
                if target2 in v:
                    target2 = k
                    break
        else:                               #높이 맞춘뒤 공통 부모노드 찾기
            target1_cnt -= 1
            target2_cnt -= 1
            for k, v in my_dict.items():
                if target1 in v:
                    target1 = k
                    break
            for k, v in my_dict.items():
                if target2 in v:
                    target2 = k
                    break
    print(target1)




if __name__ == '__main__':
    main()