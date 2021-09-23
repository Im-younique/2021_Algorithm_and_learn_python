#1, 5, 10, 25 cents 동전이 있을 때, 주어진 금액을 최소 개수의 동전으로 잔돈을 바꾸시오

def make_change(coins, target) :
    min_coins = target  #최소 동전 값이 target값이라 가정 1원으로 우다다다

    if target in coins: #target의 숫자가 coins안에 있을때 즉, target이 1,5,10,25일때
        return 1

    else:
        coins_list = list()
        for coin in coins :
            if coin <= target:
                coins_list.append(coin)
        for coin in coins_list:
            num_coins = 1 + make_change(coins, target - coin)
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins
            


def main():
    input()
    coins = list(map(int, input().split(" "))) #코인의 종류 list {1, 5, 10 ,25}
    target =  int(input())  #잔돈
    print(make_change(coins, target))

if __name__ == '__main__':
    main()