phone_num = input()

phone_num = phone_num.replace("-", "")
result = phone_num[-4:]

result = "*" * (len(phone_num)-4) + result

print(result)