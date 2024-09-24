from collections import deque

def pop(my_set, num=None):
  my_set.pop()

def discard(my_set, num=None):
  my_set.discard(num)

def remove(my_set, num=None):
  if num in my_set:
    my_set.remove(num)

def delete_from_set(callback, my_set, num=None):
  callback(my_set, num)

if __name__ == '__main__':
    n = int(input())
    elements = set(map(int, input().split()))
    num_of_operation = int(input())
    
    operations = deque()
    for i in range(0, num_of_operation):
        args = input().split()
        if len(args) == 2:
            args[1] = int(args[1])
        operations.append(args)
            
    operation_map = {
    'pop': pop,
    'discard': discard,
    'remove': remove
    }

    for el in operations:
        if len(el) == 2:
            delete_from_set(operation_map[el[0]], elements, el[1])
        else:
            delete_from_set(operation_map[el[0]], elements)

    # print(elements)
    print(sum(elements))
