# -*- coding: utf-8 -*-
from math import sqrt
#求解一元二次方程
def quadratic_equation(a, b, c):
    x1 = -1
    x2 = -1
    dirta = b*b - 4*a*c
    if dirta < 0:
        return -1
    else:
        x1 = (sqrt(dirta) - b) / (2*a)
        x2 = (-sqrt(dirta) - b) / (2*a)
    return x1,x2

print quadratic_equation(2, 3, 0)
print quadratic_equation(1, -6, 5)
#汉诺塔问题
def move(n, a, b, c):
    if n == 1:
        print a, '-->', c
        return
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)

move(2, 'A', 'B', 'C')

def average(*args):
    sum = 0.0
    n = len(args);
    for val in args:
        sum = sum + val
    if n == 0:
        return sum
    else:
        sum = sum / n
        return sum

print average()
print average(1, 2)
print average(1, 2, 2, 3, 4)
#List切片操作
L = range(1, 101)

print L[:10]
print L[2::3]
print L[4:50:5]

L = range(1, 101)
print L[-10:]
print L[-46::5]
#字符串切片
def firstCharUpper(s):
    s = s[:1].upper() + s[1:]
    return s

print firstCharUpper('hello')
print firstCharUpper('sunday')
print firstCharUpper('september')
