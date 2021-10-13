import heapq

def factory(stock, dates, supplies, import_date):
    my_count = 0
    heap = []
    index = 0

    while (stock < import_date):                          #하루에 1톤씩 사용함으로 정상적인 수입날까지의 양보다 적으면 수입을 한다.
        for i in range(index, len(dates)):      
            if dates[i] <= stock:               #반드시 수입해야한다.
                heapq.heappush(heap, (-supplies[i], supplies[i]))     #최소 힙인데 최대 힙과 같은 효과.
                index = i + 1
            else:
                break
        max_amount = heapq.heappop(heap)[1]         #양수의 힙이 나온당.
        stock += max_amount
        my_count += 1
    return my_count

def main():
    my_list = list(map(int, input().split()))    #[0]stock_now [1]k [2]date.len [3]supply.len
    date = list(map(int, input().split()))   #수입 가능한 날짜
    supplies = list(map(int, input().split())) #날짜에 따른 밀가루의 양
    

    print(factory(my_list[0], date, supplies, my_list[1]))

if __name__ == '__main__':
    main()