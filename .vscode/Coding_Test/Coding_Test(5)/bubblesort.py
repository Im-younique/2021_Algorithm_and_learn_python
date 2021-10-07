f_input = list(input().split(' '))

list = []

list = input().split(' ')

for i in range(0, int(f_input[1])):
    for j in range(0, len(list)):
        if(f_input[2] == 'A'):             ##오름차순
            if(j == 0):
                pass
            elif(list[j] < list[j-1]):
                temp = list[j]
                list[j] = list[j-1]
                list[j-1] = temp
        elif(f_input[2] == 'D'):           ##내림차순
            if(j == 0):
                pass
            elif(list[j] > list[j-1]):
                temp = list[j]
                list[j] = list[j-1]
                list[j-1] = temp


print(*list)