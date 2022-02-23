import sys

def main():
    N = int(input())
    my_list = list(map(int, sys.stdin.readline().split()))
    res = [-1] * N
    my_stack = []

    my_stack.append(0)
    for i in range(1, N):
        while my_stack and my_list[my_stack[-1]] < my_list[i]:
            res[my_stack.pop()] = my_list[i]
        my_stack.append(i)
    
    print(*res)

if __name__ == "__main__":
    main()