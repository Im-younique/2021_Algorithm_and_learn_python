import itertools

def tsp():
    n = int(input())        #노드의 갯수 입력받음
    input_list = list(map(int, input().split()))        #노드를 쌍으로 받음

    src = (input_list[0], input_list[1])          #출발지점
    dst = (input_list[2], input_list[3])          #목적지
    points = []                                   #중간에 방문하는 모든 노드
    points_sliced = input_list[4:]                #출발지 목적지를 제거한 리스트

    for i in range(0, len(points_sliced), 2):      
        #중간 노드가 len(points_slice)만큼 있고 2쌍씩 묶는다
        points.append((points_sliced[i], points_sliced[i+1]))
        #방문해야 하는 지점에 쌍의 리스트를 추가

    min_distance = float('inf')                 #찾기 원하는 값 (초기화는 무한대)
    for i in itertools.permutations(points):    #모든 points의 조합 찾기
        path = [src, *list(i), dst]             #출발지부터 목적지까지
        #*list(i) 는 list(i)의 실제 값 
        distance = 0

        for j in range(0, len(path)-1):           #경로의 모든 경우의 수
            #x는 x끼리 y는 y끼리 계산해서 거리계산
            distance += abs((path[j][0] - path[j+1][0]) + abs(path[j][1] - path[j+1][1]))

        #distance의 값 갱신
        min_distance = distance if distance < min_distance else min_distance

    return min_distance

if __name__ == "__main__":
    test_case = int(input())
    for _ in range(0, test_case):
        print(tsp())
