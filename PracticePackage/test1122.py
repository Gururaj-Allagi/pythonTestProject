newList = [12, 35, 9, 56, 24]



newList[0], newList[-1] = newList[-1], newList[0]
#
print(newList)

# lst = [15, 6, 7, 10, 12, 20, 10, 28, 10, 15]
#
# new_lst= lst[0]
# count=0
#
# for i in lst:
#     if i == new_lst:
#         count += 1
# print("{} is repeated {} times ".format(new_lst, count))

# list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
#
# new_list = list [1]
# count=0
#
# for i in list:
#     if i == new_list:
#         count += 1
# print("{} is duplicated {} times ".format(new_list, count))


# class Parent():
#     def __init__(self):
#         print("Parent")
#
#
# class Child(Parent):
#     def __init__(self):
#         Parent.__init__(self)
#         print("Child")
#
# Child()

dct = {"name": "morpheus", "job": "leader"}

print(dct.get("job"))

# print(dct["job"])
#
# di = dict()
# di["a"] = 1
# print(di)
#
# a, b = 1, 1
# output = []
# for x in range(10):
#     output.append(a)
#     a, b = b, a+b
# print(output)
#
# print(ord("a"))
#
# print(set(output))
#
# print(max(output))
#
# str = "Gururaj Allagi"
# itr = iter(str)
# print(next(itr))