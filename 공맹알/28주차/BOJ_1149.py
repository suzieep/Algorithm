n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(3): #RGB
        # 다이나믹 프로그래밍
        rgb[i][j] += min(rgb[i-1][:j]+rgb[i-1][j+1:])

print(min(rgb[-1])) 