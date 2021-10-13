import collections

def noncompletion(part, comp):
    my_list = collections.Counter(part) - collections.Counter(comp)     #key값을 비교해서 남은 key값이 my_list에 들어간다.
    return my_list

def main():
    participant = list(input().split())     #참가자 명단
    completion = list(input().split())      #완주자 명단
    
    print(*noncompletion(participant, completion))

if __name__ == '__main__':
    main()