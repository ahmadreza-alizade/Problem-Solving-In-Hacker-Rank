# eval() is usefull
if __name__ == "__main__":
    x, result_k = list(map(int, input().split()))
    print(eval(input()) == result_k)
