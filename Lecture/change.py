#1, 5, 10, 25 cents 동전이 있을 때, 주어진 금액을 최소 개수의 동전으로 잔돈을 바꾸시오

def make_change(coin_list, target) : #찾는 목표 값 target #잔돈의 종류 coin_list
    min_coins = target  #target의 값이 1원일 때

    if target in coin_list: #target의 숫자가 coins안에 있을때 즉, target이 1,5,10,25일때
        return 1

    else:
        coins = list()
        for coin in coin_list:
            if coin <= target:  #찾는 값보다 작거나 같은 잔돈종류
                coins.append(coin)
        for coin in coins:
            num_coins = 1 + make_change(coin_list, target - coin)   #재귀로 모든 경우 찾음
            if num_coins < min_coins:   #최솟값을 구하는 부분
                min_coins = num_coins
    return min_coins
            


def main():
    input()   #(사용)동전의 갯수
    coins = list(map(int, input().split(" "))) #잔돈의 종류 list {1, 5, 10 ,25}
    target =  int(input())  #찾으려는 값 ex 30 / 32
    print(make_change(coins, target))

if __name__ == '__main__':
    main()