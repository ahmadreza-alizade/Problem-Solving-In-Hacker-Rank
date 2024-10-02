import numpy as np

if __name__ == "__main__":
    dim = int(input())
    matrix = []
    for _ in range(dim):
        matrix.append(list(map(float, input().split())))
    print(round(np.linalg.det(matrix), 2))

