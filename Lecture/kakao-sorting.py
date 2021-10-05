import re

def file_name_sort(fname_list):
    p = re.compile('(\D+)(\d+)')    #정규식: 숫자아닌것 / 숫자인것

    fname_list.sort(key=lambda x: (p.match(x).group(1).lower(), int(p.match(x).group(2))))   #람다 함수를 이용한 멀티키로 정렬
    # 람다함수 매개변수 x에 match되어 정규식 group(1)은 (\D+) 소문자로하고 정렬 / 람다함수 매개변수 x에 match되어 정규식 group(2)는 (\d+) int형으로 형변환하고 정렬.
    # 결론 a~z순으로 정렬후 숫자 작은순으로 정렬된다. a.sorted(Timsort 정렬)
    return (fname_list)


if __name__ == "__main__":
    c = int(input().strip())
    for t in range(c):
        fname_list = []
        fname_list = list(x.strip() for x in input().split(','))
        result = file_name_sort(fname_list)
        print(*result)