def main():
    K = int(input())
    temp = []
    for _ in range(K):
        num = int(input())
        if num == 0:
            if len(temp) != 0:
                temp.pop()
            else:
                continue
        else:
            temp.append(num)
    
    res = 0
    if len(temp) == 0:
        print(0)
    else:
        for n in temp:
            res += n
        print(res)

if __name__ == '__main__':
    main()