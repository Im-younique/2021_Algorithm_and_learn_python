import sys

def main():
    N = int(sys.stdin.readline())
    node_list = list(map(int, sys.stdin.readline().split()))
    target = float(sys.stdin.readline())#target값
    K = int(sys.stdin.readline())       #인접한 노드 수

    my_dict = {}
    for i in node_list:
        result = abs(target-i)
        my_dict[i] = result

    my_dict = sorted(my_dict, key= lambda x : my_dict[x])       #dict의 value 절댓값 작은순으로 정렬   

    for j in range(K):  #정렬된 key값 중 작은 K개의 수 출력
        print(my_dict[j], end=" ")

    
if __name__ == "__main__":
    main()