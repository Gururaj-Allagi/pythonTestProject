def armStrong(num):
    sum = 0
    x = num
    temp = 0
    while (x != 0):
        temp = x % 10
        sum = sum + (temp*temp*temp)
        x = x//10

    return (num == sum)

print(armStrong(153))

# print(153//10)