#전화번호는 11자리 아니면 10자리

phone_num = input()

phone_num = phone_num.replace('-', '')

result = '*' * (len(phone_num) -4)

result += phone_num[-4:]
print(result)