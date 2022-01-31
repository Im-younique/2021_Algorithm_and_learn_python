import sys

def main():
    N = int(input())
    word_list = set()

    for _ in range(N):
        word = input()
        word_list.add(word)

    word_list = list(word_list)
    word_list.sort(key=lambda x : (len(x), x))

    for w in word_list:
        print(w)

if __name__ == '__main__':
    main()