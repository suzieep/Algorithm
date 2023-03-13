h,m,s = map(int,input().split())
t = int(input())

# t를 min으로 못만드는 애들을 s로 더하고
s += t % 60
t = t // 60
# t -> m으로 전환
if s >= 60:
    s -= 60
    m += 1
# t를 hour로 못만드는 애들을 m으로 더하고
m += t % 60
t = t // 60
# t -> h로 전환
if m >= 60:
    m -= 60
    h += 1

h += t % 24
if h >= 24:
    h -= 24

print(h,m,s)