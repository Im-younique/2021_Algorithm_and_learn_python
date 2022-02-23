def main():
    n = int(input())
    temp = []
    res = []
    answer = []
    my_stack = []
    temp2 = []
    for i in range(1, n+1):
        temp.append(i)
        res.append(int(input()))
    
    k = 0
    for _ in range(len(temp)):
        my_stack.append(temp[_])
        answer.append('+')
        while my_stack[-1] == res[k]:
            temp2.append(my_stack.pop())
            answer.append('-')
            k += 1
            if len(res) == k or len(my_stack) == 0:
                break
            
    if res == temp2:
        for s in answer:
            print(s)
    else:
        print("NO")

if __name__ == "__main__":
    main()