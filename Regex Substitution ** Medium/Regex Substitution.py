import re
if __name__ == "__main__":
    num_line = int(input())
    lines = [input() for _ in range(num_line)]

    pattern = r"(?<=\s)(&&|\|\|)(?=\s)"

    replacement = {"&&": "and", "||": "or"}

    def replacement_logical_operators(match):
        return f"{replacement[match.group(1)]}"

    changed_lines = [
        re.sub(pattern, replacement_logical_operators, line) for line in lines]

    for l in changed_lines:
        print(l)
