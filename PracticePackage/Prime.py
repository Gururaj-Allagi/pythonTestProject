n = 3
# print(n%2)

for a in range(2,n):
    if n%a == 0:
        print("{} is not a prime number".format(n))
        break
    else:
        print("{} is a prime number".format(n))
        break
