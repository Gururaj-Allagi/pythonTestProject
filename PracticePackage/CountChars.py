from collections import Counter

#
# str = "My name Gururaj Allagi"
#
# print(Counter(str))
#
# count = 0
# dct = {}
# for ch in str:
#     for char in str:
#         if char == ch:
#             count += 1
#             dct[char] = count
#     count = 0
#
# print(dct)
#
# for key, val in dct.items():
#     print(key, val)
#
with open ("test.txt", 'r') as reader:
    # print(reader.read())
    str = reader.read()
    # print(str)

    count = 0
    dict = {}
    for varify in str:
        for char in str:
            if char == varify:
                count = count + 1
                dict[char] = count

        count = 0
    print(dict)
    print(dict.keys())
    print(max(dict.values()))

