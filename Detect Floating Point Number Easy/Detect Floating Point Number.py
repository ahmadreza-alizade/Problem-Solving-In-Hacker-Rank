import re

if __name__ == "__main__":
    num = int(input())

    phone_number_pattern = re.compile(
        r"[+-]?(\d+\.\d+|\.\d+|\d+\.?\d+)([eE][+-]?\d+)?(?![^\d])")

    for _ in range(num):
        print(True if phone_number_pattern.match(input()) else False)
