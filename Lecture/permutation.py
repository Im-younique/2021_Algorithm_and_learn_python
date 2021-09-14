#이해가 잘 안됩니다 교슈님...
#본인의 코드로 만들어서 풀어보기.

def perm(input_list):       #n개의 정수를 나열하는 모든 경우의 수
    length = len(input_list)
    if length == 1:             #종료조건
        return [input_list]     #재귀가 끝나면 input_list배열을 반환한다.
    else:
        result = []
        for i in input_list:
            temp = input_list.copy()        #임시로 한개 선택해서 한 자리에
            print("copied input: ", temp)
            temp.remove(i)                  #임시로 선택한거 제거
            print("removed i :",temp, "i : ", i)
            for j in perm(temp):            #선택한거 제외한 나머지는 permutation
                j.insert(0, i)              
                print("inserted i : ", j)
                if j not in result:         #결과를 하나씩 추가
                    result.append(j)
    return result               #원하는 결과를 return해서 종료


if __name__ == "__main__":
    n = int(input())
    input_list = [x for x in range(1, int(n) + 1)]
    print(perm(input_list))