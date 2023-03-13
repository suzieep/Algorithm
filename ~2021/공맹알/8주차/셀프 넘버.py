n_list = list(range(1, 10001))
r_list = []
for x in n_list :
    for n in str(x):
        x += int(n)
    if x <= 10000:
        r_list.append(x)

for x in set(r_list):
    n_list.remove(x)
for x in n_list :
    print(x)