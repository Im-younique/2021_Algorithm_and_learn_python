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
