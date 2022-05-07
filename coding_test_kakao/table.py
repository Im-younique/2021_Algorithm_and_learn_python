import copy     #30점, 정확성 100%, 효율성 0%

def solution(n, k, cmd):        #k는 인덱스 넘버
    init = [i for i in range(n)]
    after = copy.deepcopy(init)
    del_list = []
    answer = []
    for c in cmd:
        if c == "C": #삭제
            del_list.append(after.pop(k))
            if len(after) == k:
                k -= 1
        elif c == "Z": #복구  넣고 소팅
            temp = del_list.pop()
            if after[k] > temp:
                k += 1
            after.append(temp)
            after.sort()
        else:
            char, num = c.split()
            if char == "D":
                k += int(num)
            else:
                k -= int(num)
    
    for i in range(n):
        if i in after:
            answer.append('O')
        else:
            answer.append('X')
    return ''.join(answer)

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(n, k, cmd))