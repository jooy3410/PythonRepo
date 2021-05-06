k, n, m = map(int, input().split())

if k*n > m:
    a = (k * n) - m
    print(a)

elif k*n <= m:
    print(0)