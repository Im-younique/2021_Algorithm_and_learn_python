
def weigth(asteroid_list):
    asteroid_list.sort()

    while(len(asteroid_list) > 1):
        a = asteroid_list.pop(len(asteroid_list) - 1)
        b = asteroid_list.pop(len(asteroid_list) - 1)
        if a == b:
            continue
        elif a > b:
            result = a - b
            asteroid_list.append(result)
        elif a < b:
            result = b - a
            asteroid_list.append(result)
        asteroid_list.sort()

    if(len(asteroid_list) == 0):
        asteroid_list.append(0)

    return asteroid_list

def main():
    asteroid_list = list(map(int, input().split()))
    
    print(*weigth(asteroid_list))


if __name__ == '__main__':
    main()