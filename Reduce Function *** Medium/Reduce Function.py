# import re
# from functools import reduce
# from math import gcd

# if __name__ == "__main__":
#     number = int(input())
#     sides = [list(map(int, input().split())) for _ in range(number)]

#     elements = list(zip(*sides))

#     up = reduce(lambda x, y: x * y, elements[0])
#     down = reduce(lambda x, y: x * y, elements[1])
#     gcd_num = gcd(up, down)
#     print(up//gcd_num, down//gcd_num)
from fractions import Fraction
from functools import reduce

def product(fracs):
    print(fracs)
    # complete this line with a reduce statement
    t = reduce(lambda x, y: x*y, fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
