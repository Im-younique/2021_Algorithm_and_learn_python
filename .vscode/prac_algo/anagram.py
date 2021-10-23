def anagram(s1, s2):
    if "".join(sorted(s1)) == "".join(sorted(s2)):
        return True
    else:
        return False


def main():
    s1, s2 = map(str, input().strip().lower().split())
    print(anagram(s1, s2))

if __name__ == "__main__":
    main()