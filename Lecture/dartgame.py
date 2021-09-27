import re

def calc_dart(input_string):
    p = re.compile("(\d+)([a-zA-Z])(\*|\#)?")   #정규식
    #(숫자하나이상)(알파벳(S,D,T))(*or#이 한개 혹은 없음) 이라는 규칙 
    score_list = p.findall(input_string)    #정규식에 맞는거 찾아서 list에 넣기

    result = [] #1회 던질 때 점수 1개가 각 index에 들어감

    for i, score in enumerate(score_list):
        #score_list의 인덱스의 번호와 컬렉션의 원소를 tuple형태로 반환
        #score_list[0] = ex)1S*
        #score_list[] 안에 score[]를 넣어줌.
        #score[0] = 숫자하나이상 / score[1] = 알파벳 score[2] = 옵션 *|#
        point = score[0]    
        bonus = score[1]
        option = score[2]
        if bonus == 'S': bonus = 1
        elif bonus == 'D': bonus = 2
        elif bonus == 'T': bonus = 3
        if option == "*":   #옵션 *
            if i == 0:  #스타상이 처음에 나오면 처음 것만 2배
                result.append(int(point)**bonus*2)
            else:   #스타상이 2,3번째에 나올시 전의 점수 2배 본인점수 2배
                result[-1] *= 2
                result.append(int(point)**bonus*2)
        elif option =="#":  #옵션 #
            result.append(int(point)**bonus*-1)
        else: result.append(int(point)**bonus) #옵션 x
    return sum(result)  #for문 끝나고 총 합 return
        
def main():
    input_count = int(input())  #Testcase 갯수

    for _ in range(0, input_count): #Testcase만큼 반복
        input_string = input().strip()  #strip함수는 문자열의 앞, 뒤 공백 제거
        print(calc_dart(input_string))

if __name__ == '__main__':
    main()