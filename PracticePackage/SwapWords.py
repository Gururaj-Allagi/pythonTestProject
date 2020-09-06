string = "My name Gururaj Allagi"
print(string)
#
spl = string.split()

# spl[2], spl[-1] = spl[-1], spl[2]
# print(" ".join(spl))
#
#
print([sent.replace("Gururaj","Allagi") if sent.find("Gururaj") >= 0 else sent.replace("Allagi","Gururaj") for sent in spl])

ll = []

for name in spl:
    if name == "Gururaj":
        ll.append(name.replace("Gururaj", "Allagi"))
    else:
        ll.append(name.replace("Allagi", "Gururaj"))
print(" ".join(ll))
