def solution(id_list, report, k):
    my_dict = dict()
    for i in range(len(id_list)):
        my_dict[id_list[i]] = 0
    my_map = [[] for _ in range(len(id_list))]  #각 자리수에 맞게 신고한 사람 들어감
    report = list(set(report))      #중복처리
    
    for r in report:
        send, recv = r.split()
        my_map[id_list.index(recv)].append(send)
        my_dict[recv] += 1
    answer = [0] * len(id_list)   #결과 메일 수
    for j in id_list:
        if my_dict[j] >= k:
            reporter = my_map[id_list.index(j)]
            for r in reporter:
                answer[id_list.index(r)] += 1    
            
    return answer

def main():
    id_list= ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    k = 2

    print(solution(id_list, report, k))

if __name__ == "__main__":
    main()