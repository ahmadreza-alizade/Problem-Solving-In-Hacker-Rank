import re
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

regex = re.compile(r'(?<=\w)([\W]+)(?=\w)')
matrix = [None] * n * m

for x in range(n):
    matrix_item = [x for x in input()]
    for y in range(m):
        matrix[x+(n*y)] = matrix_item[y]
 
print(re.sub(regex, ' ', ''.join(matrix)))

import re

if __name__ == "__main__":
    n_list, m_index = list(map(int, input().split()))
    rows = []

    for _ in range(n_list):
        l = list(input())
        rows.append(l)
    regex = re.compile(r'(?<=\w)([\W]+)(?=\w)')
    pure_str = "".join("".join(list(t)) for t in list(zip(*rows)))
    modified_string = str(re.sub(regex, ' ', pure_str))
    # modified_string = re.sub(r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])', " ", pure_str)
    print(modified_string)
