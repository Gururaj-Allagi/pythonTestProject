list = [3, 4, 5, 6, 7, 8, 9]

r = 2

for a in range(0, r):
    list.append(list[0])
    del list[0]

print(list)
