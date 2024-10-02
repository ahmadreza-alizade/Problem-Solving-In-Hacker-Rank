import numpy as np

if __name__ == "__main__":
    coefficients = list(map(float, input().split()))
    value = float(input())
    
    result = np.polyval(coefficients, value)
    print(result)
    
