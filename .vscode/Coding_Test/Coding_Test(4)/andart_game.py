import re

def dart_score(s):
    p = re.compile("(\d+)([a-zA-Z])(\*|\#)?")   #정규식
    #(숫자하나이상)(알파벳(S,D,T))(*or#이 한개 혹은 없음) 이라는 규칙 
    score_list = p.findall(s)

    result = []
    has_star = False    #이전에 *가 있었는가를 판단하는 has_star
    for i, score in enumerate(score_list):
        #score_list의 인덱스의 번호와 컬렉션의 원소를 tuple형태로 반환
        #score_list[0] = ex)1S*
        #score_list[] 안에 score[]를 넣어줌.
        #score[0] = 숫자하나이상 / score[1] = 알파벳 score[2] = 옵션 *|#
        point = score[0]    
        bonus = score[1]
        option = score[2]
        if bonus == 'S':  bonus = 1
        elif bonus == 'D' : bonus = 2
        elif bonus == 'T' : bonus = 3
        if option == '*':
            if i == 2:  #마지막 스타는 본인 것만 두배
                result.append(int(point)**bonus*2)
            else:
                if has_star:    #본인이 스타를 가지고 이전에 스타가 있다면 4배!
                    result.append(int(point)**bonus*4)
                    has_star = True
                else:           #본인이 스타를 가졌다
                    result.append(int(point)**bonus*2)
                    has_star = True #다음것을 비교할 때 전에 star있다고 나타냄
        elif option == '#':
            if i == 0:
                result.append(int(point)**bonus*(-1))
            else:
                if has_star:    #이전에 스타가 있으면 -2배
                    result.append(int(point)**bonus*(-2))
                    has_star = False    #이번에는 #이므로 star는 없다
                else:
                    result.append(int(point)**bonus*(-1))
        else:
            if i == 0:
                result.append(int(point)**bonus)
            else:
                if has_star:    #이전에 스타가 있으면 2배
                    result.append(int(point)**bonus*2)
                    has_star = False
                else:
                    result.append(int(point)**bonus)
    return sum(result)

str = input().strip()

print(dart_score(str))
                

           