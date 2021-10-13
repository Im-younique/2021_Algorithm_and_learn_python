
def weigth(asteroid_list):
    asteroid_list.sort()                            #소팅

    while(len(asteroid_list) > 1):
        a = asteroid_list.pop(len(asteroid_list) - 1)   #소팅한 배열의 큰값은 len()-1에 있고 빼낸다.
        b = asteroid_list.pop(len(asteroid_list) - 1)
        if a == b:      #두 개의 무게가 같으면 빼낸채로 종료한다.
            continue
        elif a > b:     #a가 크면 빼서 남은 값을 다시 배열에 넣는다.
            result = a - b
            asteroid_list.append(result)
        elif a < b:     #이거 왜했지..?(안해도 된다. 왜냐하면 소팅하면 어차피 a가 큰 값이다.)
            result = b - a
            asteroid_list.append(result)
        asteroid_list.sort()    #새로운 값을 위한 소팅

    if(len(asteroid_list) == 0):    #둘 다 사라져서 배열이 비어있으면 0을 추가한다.
        asteroid_list.append(0)

    return asteroid_list

def main():
    asteroid_list = list(map(int, input().split()))     #소행성 정수
    
    print(*weigth(asteroid_list))


if __name__ == '__main__':
    main()