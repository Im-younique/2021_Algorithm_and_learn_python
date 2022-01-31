import sys

def main():
    N = int(input())
    dot_list = list(map(int, sys.stdin.readline().split()))
    temp = set()
    for i in dot_list:
        temp.add(i)

    temp = list(temp)
    temp.sort()

    my_dict = {}
    for i in range(len(temp)):
        my_dict[temp[i]] = i
    
    for r in range(len(dot_list)):
        dot_list[r] = my_dict[dot_list[r]]

    print(*dot_list)

if __name__ == '__main__':
    main()