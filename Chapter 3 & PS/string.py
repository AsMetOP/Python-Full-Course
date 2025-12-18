name = "Asmet"
# 0 -> 1 -> 2 -> 3 ....
# .... -4 <- -3 <- -2 <- -1

nameshort = name[0:3]
print(nameshort)

nameshort2 = name[-5:-2]
print(nameshort2)

Char1 = name[1]
print(Char1)

Char2 = name[-1]
print(Char2)

Char2 = name[4]
print(Char2)

name2 = "Vishwanath"
print(name2[1:7:2])

print(len(name), '&' ,len(name2))
print(name.endswith("met"))
print(name2.endswith("met")) 
print(name.startswith("As")) 
print(name.startswith("vis"))


