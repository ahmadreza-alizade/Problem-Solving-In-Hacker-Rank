
if __name__ == "__main__":
    stu_num, subjects_num = list(map(int, input().split()))

    result = []
    for _ in range(subjects_num):
        result.append(list(map(float, input().split())))

    final_list = zip(*result)

    avg_list = list(map(lambda l: round(sum(l)/len(l), 1), final_list))

    for avg in avg_list:
        print(avg)
