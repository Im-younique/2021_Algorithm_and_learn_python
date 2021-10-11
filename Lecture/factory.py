import heapq

def factory(stock, dates, supplies, k):
    import_count = 0
    stock_heap = []
    index = 0

    while (stock < k):                          #하루에 1톤씩 사용함으로 정상적인 수입날까지의 양보다 적으면 수입을 한다.
        for i in range(index, len(dates)):      
            if dates[i] <= stock:               #반드시 수입해야한다.
                heapq.heappush(stock_heap, (-supplies[i], supplies[i]))     #최소 힙인데 최대 힙과 같은 효과.
                index = i + 1
            else:
                break
        max_amount = heapq.heappop(stock_heap)[1]
        stock += max_amount
        import_count += 1
    return import_count

def main():
    initial_amount = int(input())               #초기 남은 밀가루의 양 (하루에 1톤씩 사용함)
    import_date = list(map(int, input().split()))   #수입 가능한 날짜
    import_amount = list(map(int, input().split())) #날짜에 따른 밀가루의 양
    regular_import_date = int(input())              #정상적으로 수입가능한 날짜.

    print(factory(initial_amount, import_date, import_amount, regular_import_date))

if __name__ == '__main__':
    main()