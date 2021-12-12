import sys

def lis(N, my_arr):
    cur_arr = []
    cur_arr.append(my_arr[0])
    lower_bound = my_arr[0]+1
    for i in range(1, N):
        if(my_arr[i] > cur_arr[len(cur_arr)-1]):        #현재 값이 배열의 마지막 원소보다 크면
            cur_arr.append(my_arr[i])
        else:                                           #이분탐색 해야하지만, lowerbound 위치의 값을 대체하는 부분
            for j in range(len(cur_arr)):
                if(cur_arr[j] > my_arr[i]):
                    if(cur_arr[j-1] < my_arr[i] or j-1 < 0):
                        cur_arr[j] = my_arr[i]
                        break
                else:
                    continue
    
    return len(cur_arr)

def main():
    N = int(sys.stdin.readline())
    my_arr = list(map(int, sys.stdin.readline().split()))
    print(lis(N, my_arr))
if __name__ == '__main__':
    main()