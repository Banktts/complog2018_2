def make_int_list(x):
    return [int(i) for i in x.strip().split()]
def is_odd(e):
    return True if e % 2 != 0 else False
def odd_list(alist):
    return list(filter(lambda x: x != None, [int(i) if is_odd(i) else None for i in alist]))
def sum_square(alist):
    return sum(list(map(lambda x: x*x, alist)))
exec(input().strip())
