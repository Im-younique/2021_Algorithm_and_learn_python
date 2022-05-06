def solution(new_id):
    new_id = list(new_id.lower())
    temp = []
    for i in range(len(new_id)):
        flag = True
        if not(new_id[i].isdigit() or new_id[i].islower() or new_id[i] == '-' or new_id[i] == '_' or new_id[i] == '.'):
            flag = False
        if len(temp) != 0 and temp[len(temp)-1] == "." and new_id[i] == ".":
            flag = False
        if flag:
            temp.append(new_id[i])

    while len(temp) != 0 and (temp[0] == "." or temp[len(temp)-1] == "."):
        if temp[0] == ".":
            temp = temp[1:]
        else:
            temp = temp[0:len(temp)-1]

    #new_id = "".join(temp)
    new_id = temp
    if len(new_id) == 0:
        new_id.append("a")
    elif len(new_id) >= 16:
        new_id = new_id[0:15]
        for j in range(len(new_id)-1, 0, -1):
            if new_id[j] == ".":
                new_id = new_id[0:j]
            else:
                break
    
    if len(new_id) <= 2:
        alpha = new_id[len(new_id)-1]
        while len(new_id) < 3:
            new_id.append(alpha)
    
    answer = "".join(new_id)
    return answer

def main():
    new_id = "-.~!@#$%&*()=+[{]}:?,<>/.-"
    print(solution(new_id))

if __name__ == '__main__':
    main()