#사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙 1 : http:// 부분은 제외 => naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e'갯수 + "!" 로 구성

# 예) 생성된 비밀번호 : nav51!

page = "http://naver.com"
url = page
page = page.replace("http://", "")      #규칙1
index = page.index(".")
page = page.replace(page[index:], "")   #규칙2

#page = page[:page.index(".")] #규칙 2

length = len(page)              #규칙 3
number_of_e = page.count("e")
page = page[:3]                 
print("{0}의 비밀번호는 {1} 입니다.".format(url, page+str(length)+str(number_of_e)+"!"))
