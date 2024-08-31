import itertools


def exp(selections, m_const):
    sum = 0
    for i in selections:
        sum = sum + i**2
    return sum % m_const


elements = []
rows_list = []
if __name__ == "__main__":
    first_input = input().split(" ")
    m_const = int(first_input[1])
    row_len_const = int(first_input[0])
    for _ in range(0, int(first_input[0])):
        row_list = list(map(int, input().split()))
        row_list.pop(0)
        rows_list.append(row_list)

    # important part
    combinations = list(list(each_tuple)
                        for each_tuple in itertools.product(*rows_list))
    finals = []
    for item in combinations:
        finals.append(exp(item, m_const))
    print(max(finals))
