for x in range(5):
    for y in range(x+1):
        print('*', end= ' ')
    print(' ')

a=1
for x in range(5):
    for y in range(x+1):
        print(a, end= ' ')
    a+=1
    print(' ')

b=1
for x in range(5):
    for y in range(x+1):
        print(b, end= ' ')
        b+=1
    print(' ')

print("guru {}".format(b))