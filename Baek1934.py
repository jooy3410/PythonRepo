n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    #기존의 값을 복사해둠
    x = a
    y = b
    while b != 0:
        r = a % b
        a = b
        b = r
    gcd = a
    lcd = x * y / a
    print(int(lcd))