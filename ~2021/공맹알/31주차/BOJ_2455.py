on = []
ppl = 0

for i in range(4):
    a, b = map(int, input().split())
    ppl += b # b만큼타고
    ppl -= a # a만큼 내리고
    on.append(ppl) #저장

print(max(on))