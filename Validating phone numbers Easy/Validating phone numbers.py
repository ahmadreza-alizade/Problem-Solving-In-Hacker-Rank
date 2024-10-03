import re

if __name__ == "__main__":
    num = int(input())

    phone_number_pattern = re.compile(
        r"^[7|8|9]\d{9}$")

    for _ in range(num):
        print("YES" if phone_number_pattern.match(input()) else "NO")
