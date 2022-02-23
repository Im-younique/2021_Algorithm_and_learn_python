import sys

def main():
    hour, min = map(int, sys.stdin.readline().split())
    p_min = int(input())

    p_hour = int((min + p_min) / 60)
    r_min = (min + p_min) % 60
    r_hour = hour + p_hour
    if r_hour >= 24:
        r_hour = r_hour % 24

    print(r_hour, r_min)

if __name__ == "__main__":
    main()