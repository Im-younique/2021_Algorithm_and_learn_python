def solution(record):
    answer = []
    my_dict = dict()
    for r in record:
        if r.split()[0] == "Enter":
            my_dict[r.split()[1]] = r.split()[2] + "님이"
            answer.append(r.split()[1] + " 들어왔습니다.")
        elif r.split()[0] == "Leave":
            answer.append(r.split()[1] + " 나갔습니다.")
        elif r.split()[0] == "Change":
            my_dict[r.split()[1]] = r.split()[2] + "님이"
    
    for i in range(len(answer)):
        answer[i] = my_dict[answer[i].split()[0]] + " " + answer[i].split()[1]
    
    return answer

def main():
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    print(solution(record))

if __name__ == "__main__":
    main()