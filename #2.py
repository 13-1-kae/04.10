    def r(n):
    t = []
    for i in range(n):
        if i == 0 or i == n-1:
            t.append(1)
        else:
            k = r(n-1)
            t.append(k[i-1]+k[i])
    return t
def triangle(x):
    for i in range(x):
        print(r(i+1))
    return ' '
a = int(input())
print(triangle(a+1))
