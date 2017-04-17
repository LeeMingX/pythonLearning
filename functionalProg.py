from math import sqrt

def add(x, y, f):
    return f(x) + f(y)

print add(25, 9, sqrt)

def calc_prod(lst):
    def mul(x, y):
        return x * y
    def delay_calc():
        x = reduce(mul, lst)
        return x
    return delay_calc

f = calc_prod([1,2,3,4]);
print f()

def count():
    fs = []
    for i in range(1, 4):
        def f(n):
            def g():
                return n * n
            return g
        r = f(i)
        fs.append(r)
    return fs

f1, f2, f3 = count()
print f1(), f2(), f3()
