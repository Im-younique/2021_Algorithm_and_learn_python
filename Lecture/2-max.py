n = int(input())

for _ in range(0, n) :
    int_list = list(map(int, input().split()))
    # #print(max(int_list))

    # temp_max= int_list[0]     #O(n)의 복잡도
    # for i in int_list:
    #     if(temp_max < i ) :
    #         temp_max = i
    # print(temp_max)

    # ↓ sorting   O(n log n)의 복잡도 ↓
    int_list.sort()
    print(int_list[len(int_list) -1])