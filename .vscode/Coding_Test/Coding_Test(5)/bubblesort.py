f_input = list(input().split(' '))          #배열의 수, 출력할 순서, 오름차순 혹은 내림차순 차례로 받아 list에 넣는다.

list = []

list = input().split(' ')

for i in range(0, int(f_input[1])):         #출력할 순서까지만 
    for j in range(0, len(list)):
        if(f_input[2] == 'A'):             ##오름차순 버블 소트
            if(j == 0):
                pass
            elif(list[j] < list[j-1]):
                temp = list[j]
                list[j] = list[j-1]
                list[j-1] = temp
        elif(f_input[2] == 'D'):           ##내림차순 버블 소트
            if(j == 0):
                pass
            elif(list[j] > list[j-1]):
                temp = list[j]
                list[j] = list[j-1]
                list[j-1] = temp

#출력할 순서까지 소팅된 리스트 출력
print(*list)