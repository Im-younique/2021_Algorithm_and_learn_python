import collections

def noncompletion(part, comp):
    my_list = collections.Counter(part) - collections.Counter(comp)
    return my_list

def main():
    participant = list(input().split())
    completion = list(input().split())
    
    print(*noncompletion(participant, completion))

if __name__ == '__main__':
    main()