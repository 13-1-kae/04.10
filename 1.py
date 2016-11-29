__author__ = 'student'
def  fib(n):
    assert n >=0
    if n<=2:
        return 1
    return fib(n-1) + fib (n-2)


a=int(input())
d=fib(a)
print(d)