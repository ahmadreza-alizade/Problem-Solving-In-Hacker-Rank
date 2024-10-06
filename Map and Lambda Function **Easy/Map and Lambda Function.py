cube = lambda x: x ** 3

def fibonacci(n):
    if n == 0:
        return([])
    elif n == 1:
        return([0])
    fib_list = [0, 1]  # Start with the first two Fibonacci numbers
    list(map(lambda _: fib_list.append(
        fib_list[-1] + fib_list[-2]), range(2, n)))
    return fib_list

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
