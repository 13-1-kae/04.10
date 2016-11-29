n = int(input())
A = list(map(int, input().split( )))
for i in range(n):
    b = 0
    m = 0
    for j in range(n):
        if A[j] > A[i]:
            b += 1
        if A[j] < A[i]:
            m += 1
    if b == m:
        print(A[i])
        exit(0)