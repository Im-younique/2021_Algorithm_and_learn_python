# print(abs(-5))      #절댓값
# print(pow(4, 2))    #제곱
# print(max(5, 12))   #최대값
# print(min(5, 12))   #최솟값
# print(round(3.14)) #반올림
# print(round(4.99))

# from math import *  #math에 있는 모든 함수 불러오기
# print(floor(4.99)) #내림
# print(ceil(4.99))   #올림
# print(sqrt(16)) # 제곱근

# from random import *

# print(random())     #0.0 ~ 0.1 미만 임의의 값 생성
# print(random() * 10) #0.0 ~ 10.0 미만 임의의 값 
# print(int(random() * 10)) # 0 ~ 10 미만 임의의 값
# print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값

# print(randrange(1 , 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randint(1, 45)) #1 ~ 45 이하의 임의의 값 생성

#----------------------------------------------------------------

# sentence = "나는 소년입니다."
# print(sentence)
# sentence2 = '파이썬은 쉬워요'
# print(sentence2)
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)

#---------------------------------------------------------------

# jumin = "990902-1234567"

# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2])  #0부터 2직전까지
# print("월 : " + jumin[2:4])  #2부터 4직전까지
# print("일 : " + jumin[4:6])  #4부터 6직전까지

# print("생년월일 : " + jumin[:6]) #처음부터 6직전까지
# print("뒤 7자리 :" + jumin[7:]) #7부터 끝까지
# print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) #맨 뒤에서 7번째부터 끝까지

#---------------------------------------------------------------

# python = "Python is Amazing"
# print(python.lower()) #소문자로 적기
# print(python.upper()) #대문자로 적기
# print(python[0].isupper()) #첫글자가 대문자인가?
# print(len(python)) #문자열 길이 반환
# print(python.replace("Python", "Java")) #repalce 문자 변환

# index = python.index("n")
# print(index) #n이라는 문자가 몇번째에 있는지
# index = python.index("n", index+1)
# print(index) #첫번째 n의 위치부터 다음 n의 위치 찾기

# print(python.find("JAVA")) #문자열 위치 찾기 없으면 -1반환
# # print(python.index("JAVA")) #error

# print(python.count("n")) #n이 몇번 나오는지

#---------------------------------------------------------------

# #문자열 포맷
# #방법 1
# print("나는 %d살 입니다" %23)
# print("나는 %s을 좋아해요" %"파이썬")
# print("Apple 은 %c로 시작해요" %"A")
# # %s로만 써도 가능하다.
# print("나는 %s색과 %s색을 좋아해요" %("파란", "빨간"))

# #방법 2
# print("나는 {}살 입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요".format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요".format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨간"))

# #방법 3
# print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color="빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요".format(color="빨간", age = 20))

# #방법 4 (v 3.6이상)
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.") #f라고 쓰면 실제 변수 값을 사용

#---------------------------------------------------------------

# print("백문이 불여일견 \n 백견이 불여일타") #\n은 개행

# print('저는 "나도코딩"입니다.')
# print("저는 \"나도코딩\"입니다.")   #\"문장내에 따옴표 사용

# # \\ : 문장 내에서 \
# print("C:\\Users\\dyyim\\OneDrive\\바탕 화면\\Coding\\vscode")

# print("Red Apple\rPine") #\r : 커서를 맨 앞으로 이동

# # \b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple")

# # \t : 탭
# print("Red\tApple")

#---------------------------------------------------------------

# 리스트 [] 순서를 가진 객체의 집합

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# #조세호씨가 어디에 타고 있는가
# print(subway.index("조세호"))

# # 하하씨가 다음 정류장에서 다음 칸에 탔다
# subway.append("하하") #appned는 리스트에 추가
# print(subway)

# # 정형돈씨를 유재석 / 조세호 사이에 태워봄
# subway.insert(1, "정형돈")
# print(subway)

# # 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop())     #뒤에 한명 꺼냄
# print(subway)

# # 같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway.count("유재석"))

# #정렬도 가능
# num_list = [5, 2, 4, 3, 1]
# num_list.sort()
# print(num_list)

# #순서 뒤집기 가능
# num_list.reverse()
# print(num_list)

# #모두 지우기
# num_list.clear()
# print(num_list)

# num_list = [5, 2, 4, 3, 1]
# mix_list = ["조세호", 20, True]
# print(mix_list)

# # 리스트 확장
# num_list.extend(mix_list)
# print(num_list)

#---------------------------------------------------------------

#사전 (key:value)

# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet[5]) #오류(error)
# prnit(cabinet.get(5)) #값이 없으면 None이 나옴
# print(cabinet.get(5, "사용 가능")) #사용 가능이 default

# print(3 in cabinet) # Ture
# print(5 in cabinet) # False

# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# # 새로운 손님이 왔다

# cabinet["A-3"] = "김종국"   #업데이트
# cabinet["C-20"] = "조세호"  #추가
# print(cabinet)

# # 손님이 갔다

# del cabinet["A-3"]
# print(cabinet)

# # key 들만 출력
# print(cabinet.keys())

# # value 들만 출력
# print(cabinet.values())

# # key, value 쌍으로 출력
# print(cabinet.items())

# # 목욕탕 폐점
# cabinet.clear()
# print(cabinet)

#----------------------------------------------------------------

#튜플 -> 변경되지 않는 리스트 (속도가 빠름)

# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)

#---------------------------------------------------------------

# 집합 (set) -> 중복이 안되고 순서가 없음

# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# # 교집합 (java 와 python을 모두 하는 개발자 출력)
# print(java & python)
# print(java.intersection(python))        #intersection교집합

# # 합집합 (java를 할 수 있거나 python 할 수 있는 개발자)
# print(java | python)
# print(java.union(python))               #union합집합

# # 차집합 (java는 할 줄 알지만 python을 할 줄 모르는 개발자)
# print(java - python)
# print(java.difference(python))

# # python을 할 줄 아는 사람이 늘어남 (교육으로 인해)
# python.add("김태호")
# print(python)

# # java를 까먹음
# java.remove("김태호")
# print(java)

#---------------------------------------------------------------

# # 자료구조의 변경
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)           #list형으로 변경
# print(menu, type(menu))

# menu = tuple(menu)          #tuple형으로 변경
# print(menu, type(menu))

# menu = set(menu)            #set형으로 변경
# print(menu, type(menu))

#----------------------------------------------------------------

# 조건문

#weather = input("오늘 날씨는 어때요? ")
# if 조건 :
#     실행 명령문

# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else :
#     print("준비물이 필요 없어요")

# temp = int(input("기온은 어때요?"))
# if 30 <= temp:
#     print("너무 더워요, 나가지 마세요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp and temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")

#-----------------------------------------------------------------

#반복문 for

# for wating_no in [0,1,2,3,4] :
#     print("대기번호 : {0}".format(wating_no))

# for wating_no in range(5): #0,1,2,3,4
#     print("대기번호 : {0}".format(wating_no))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

#-----------------------------------------------------------------

#반복문 while

# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")

# customer = "아이언맨"
# index = 1
# while Ture:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))
#     index += 1

# customer = "토르"
# person = "Unknown"

# while person != customer :
#     print("{0}, 커피가 준비 되었습니다".format(customer))
#     person = input("이름이 어떻게 되세요? ")

#-----------------------------------------------------------------

#continue 와 break

# absent = [2, 5] #결석
# no_book = [7] #책을 안가져옴
# for student in range(1, 11): #1,2,3,4,5,6,7,8,9,10
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지, {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

#-----------------------------------------------------------------

#한 줄 for 문


# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# #학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

# #학생 이름을 대문자로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)

#-----------------------------------------------------------------

# 함수, 반환값

# def open_account(): 
#     print("새로운 계좌가 생성되었습니다.")

# def deposit(balance, money): #입금
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
#     return balance + money

# def withdarw(balance, money): #출금
#     if balance >= money: #잔액이 출금보다 많을 때
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance

# def withdarw_night(balance, money): #저녁에 출금
#     commision = 100 #수수료 100원
#     return commision, balance - money - commision   #return 여러개의 값 가능

# balance = 0 #잔액
# balance = deposit(balance, 1000)
# # balance = withdarw(balance, 2000)
# # balance = withdarw(balance, 500)
# commision, balance = withdarw_night(balance, 500)
# print("수수료 {0}원이며, 잔액은 {1} 원 입니다.".format(commision, balance))

#------------------------------------------------------------------

#함수에서의 기본값

# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이: {1}\t주 사용 언어:  {2}" \
#         .format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

#같은 학교 같은 학년 같은 반 같은 수업.

# def profile(name, age=17, main_lang="python"):          #전달받지 않을때 나이 17 주 언어 python
#     print("이름 : {0}\t나이: {1}\t주 사용 언어:  {2}" \
#         .format(name, age, main_lang))

# profile("유재석")
# profile("김태호")

#--------------------------------------------------------------------

#키워드 값을 이용하는 함수

# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name = "유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25, name="김태호")

#--------------------------------------------------------------------

#가변인자를 인용한 함수 호출

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") #end=" " 줄바꿈을 하지 않고 출력함
#     print(lang1, lang2, lang3, lang4, lang5)


# def profile(name, age, *language):      #가변인자 사용
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     for lang in language :
#         print(lang, end = " ")
#     print()

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
# profile("김태호", 25, "Kotiln", "Swift")

#---------------------------------------------------------------------

#지역변수와 전역변수

# gun = 10

# def checkpoint(soldiers): #경계근무
#     global gun #전역 공간에 있는 gun 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))        #bed code

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun                                          #good code

# print("전체 총 : {0}".format(gun))
# # checkpoint(2)
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))

#----------------------------------------------------------------------

#표준 입출력

# print("Python", "Java", sep=",", end="?")    #sep= 는 ,사이에 무엇을 넣을지 정함
# print("무엇이 더 재밌을까요?")                  #end=는, 마지막의 줄바꿈을 "?"로 바꾼것.

# import sys
# print("Python", "Java", file=sys.stdout)        #표준출력
# print("Python", "Java", file=sys.stderr)        #표준에러

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, socre in scores.items():            #.items() 키와 벨류 페어로 나옴
#     # print(subject, socre)
#     print(subject.ljust(8), str(socre).rjust(4), sep=":") #.ljust(8) 왼쪽정렬 8개공간 확보
#                                                           #r.just(4) 오른쪽정렬 4개공간 확보

#은행 대기순번표
#001, 002, 003, ...
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))        #.zfill(3) 3크기 만큼의 공간을 확보하고 
#                                                     #숫자를 넣는데 값이 없는 공간은 0으로 채워라

# answer = input("아무값이나 입력하세요 : ")             #사용자 입력으로 값을 받으면 항상 str형
# print(type(answer))
# # print("입력하신 값은 " + answer + "입니다.")

#--------------------------------------------------------------------------

# #다양한 출력 포멧

# # 빈 자라는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))       #{ } 안에 있는 것 ↑

# # 양수일 때 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))

# # 왼쪽 정렬하고, 빈칸을 _로 채움
# print("{0:_<10}".format(500))

# # 큰 수 일때 3자리 마다 콤마 찍기
# print("{0:,}".format(1000000000))

# # 3자리 마다 콤마를 찍는데, +- 부호도 붙이기
# print("{0:+,}".format(1000000000))
# print("{0:+,}".format(-1000000000))

# # 3자리마다 콤마를 찍는데, 부호도 붙이고, 자릿수 확보하기
# # 돈이 많으면 행복하니까 빈 자리는 ^로 채워주기
# print("{0:^<+30,}".format(1000000000))

# # 소수점 출력
# print("{0:f}".format(5/3))

# # 소수점 특정 자리수까지만 표시 (소수점 셋째 자리에서 반올림)
# print("{0:.2f}".format(5/3))

#---------------------------------------------------------------------------

#파일 입출력

# score_file = open("score.txt", "w", encoding="utf8")        #utf8은 한글 정보
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")        #입력
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")          #출력
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline()) #줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline()) 
# print(score_file.readline()) 
# print(score_file.readline()) 
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() #list 형태로 저장
# for line in lines:
#     print(line, end="")

# score_file.close()

#----------------------------------------------------------------------------

#피클

# import pickle
# # profile_file  = open("profile.pickle", "wb")        #w쓰기 b는 바이너리 피클에서 필요 인코딩 x
# # profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# # print(profile)
# # pickle.dump(profile, profile_file)  # profile에 있는 정보를 file에 저장
# # profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)     #file에 있는 정보를 profile 에 불러오기
# print(profile)
# profile_file.close()

#------------------------------------------------------------------------------

# with

# import pickle

# with open("profile.pickle", "rb") as profile_file:      #파일을 열어서 profile_file에 저장
#     print(pickle.load(profile_file))                #파일을 따로 닫지 않아도 괜찮음

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())

#-------------------------------------------------------------------------------

# 클래스

# # 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
# name = "마린" #유닛의 이름
# hp = 40     #유닛의 체력
# damage = 5  #유닛의 공격력

# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))


# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(\
#         name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)
#유닛은 엄청 많아진다.. 붕어빵 틀로 바꾸자

#일반 유닛
# class Unit:                         #부모 클래스
#     def __init__(self, name, hp, speed):                  #__init__ 생성자 (파라미터가 일치해야함)
#         self.name = name            #멤버변수(Attack 유닛과 겹침 -> 상속)
#         self.hp = hp                #멤버변수(Attack 유닛과 겹침 -> 상속)
#         self.speed = speed

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
        

# #공격 유닛
# class AttackUnit(Unit):             #(Unit 상속)자식 클래스
#     def __init__(self, name, hp, speed, damage):                   
#         Unit.__init__(self, name, hp, speed)                #상속 받은 것 초기화
#         self.damage = damage        
    
#     def attack(self, location):         #this is method
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}] "
#             .format(self.name, location, self.damage))      #self가 있으면 class 내부에 있는 변수 값을 쓴다.

#     def damaged(self, damage):          #this is method
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다".format(self.name, self.hp))
#         if self.hp <=0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# #날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# #공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):       #다중 상속
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 speed 0
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):                       #메소드 오버라이딩 move() 재정의
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# # 건물
# class BulidingUnit(Unit):
#     def __init__(self, name, hp, location):
#         #Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0)           #super를 사용할때는 ()하고 self를 쓰지않는다. / 다중 상속에서는 super는 맨 처음 상속받는 것만 호출받는다.
#         self.location = location

# # 서플라이 디폿 : 건물, 1개 건물 = 8 유닛.
# supply_depot = BulidingUnit("서플라이 디폿", 500, "7시")

# def game_start():                                     #패스 활용법
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass                                  #패스(아무것도 안하고 일단 넘어간다 / (함수) 완성된것 처럼 보이게함)

# game_start()
# game_over()

# # 벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# # 배틀크루저 : 공중 유닛, 체력도 굉장히 좋고, 공격력도 좋음
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")                         #재정의 한 무브.

# # 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)     #다중 상속 예.
# valkyrie.fly(valkyrie.name, "3시") 

# 드랍쉽 : 공중 유닛, 수송기. 마린/ 파이어뱃/ 탱크 등을 수송. 공격 x

# #메딕 : 의무병 

# #파이어뱃 : 공격 유닛, 화염방사기.
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)


# marine1= Unit("마린", 40, 5)                                #객체 
# marine2= Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# # 레이스 : 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))     #멤버변수를 외부에서 쓸 수 있다.

# # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True                 #객체에 추가로 변수를 외부에서 만들어서 사용가능

# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

#----------------------------------------------------------------------------


