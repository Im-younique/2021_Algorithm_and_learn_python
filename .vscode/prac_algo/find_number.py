
def binarysearch(sorted_list, target):          #이진 탐색
    start = 0
    end = len(sorted_list) - 1

    while start <= end:                         #시작점과 end지점이 만나면 못 찾은 거(탈출)
        mid = (start + end) // 2                #시작점과 end의 중간지점

        if sorted_list[mid] == target:          #중간지점에 target이 있으면 찾았음.
            return print(1)
        elif sorted_list[mid] < target:         #중간지점이 target값보다 작으면 위에 부분을 찾아야함.
            start = mid + 1     
        else:                                   #중간지점이 target보다 크면 아래 부분을 찾아야함.
            end = mid - 1
    
    return print(0)     #못찾으면 0
    

def main():
    N = int(input())
    n_list = list(input().split())
    n_list.sort()
    M = int(input())
    m_list = list(input().split())

    for i in m_list:
        binarysearch(n_list, i)



if __name__ == '__main__':
    main()