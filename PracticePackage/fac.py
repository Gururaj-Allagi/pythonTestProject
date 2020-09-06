result = []


def fact(num):
    if num == 0:
        result = 1
    else:
        result = num * fact(num - 1)

    return result


f = fact(4)

print(f)
