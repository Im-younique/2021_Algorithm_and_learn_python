#전화번호는 11자리 아니면 10자리

phone_num = input()

phone_num = phone_num.replace('-', '')  #하이픈 제거

result = '*' * (len(phone_num) -4)  #맨 뒷자리 4개 제외한 숫자 *표

result += phone_num[-4:]    #맨 뒷자리 4개를 이어붙임.
print(result)