H, M = map(int, input().split())
timer = int(input())

H += timer // 60
M += timer % 60

if M >= 60:
    H = H+1
    M = H - 60

if H >= 24:
    H -= 24

print(H,M)
