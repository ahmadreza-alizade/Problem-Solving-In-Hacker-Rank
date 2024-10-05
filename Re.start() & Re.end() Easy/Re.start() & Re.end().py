import re


def find_substring_indices(s, k):
    matches = re.finditer(f'(?={k})', s)
    result = [(match.start(), match.start() + len(k) - 1)
              for match in matches]
    return result


if __name__ == "__main__":

    s = input()
    k = input()

    result = find_substring_indices(s, k)
    if len(result) == 0:
        print((-1, -1))
    else:
        for start, end in result:
            print(f"({start}, {end})")
