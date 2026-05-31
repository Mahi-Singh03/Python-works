# Operators in Python

a = 10
b = 3


print("----- Arithmetic Operators -----")
print("a + b ->", a + b)
print("a - b ->", a - b)
print("a * b ->", a * b)
print("a / b ->", a / b)
print("a // b ->", a // b)
print("a % b ->", a % b)
print("a ** b ->", a ** b)
print()


print("----- Comparison Operators -----")
print("a == b ->", a == b)
print("a != b ->", a != b)
print("a > b ->", a > b)
print("a < b ->", a < b)
print("a >= b ->", a >= b)
print("a <= b ->", a <= b)
print()


print("----- Logical Operators -----")
x = True
y = False

print("x and y ->", x and y)
print("x or y ->", x or y)
print("not x ->", not x)
print()


print("----- Assignment Operators -----")
c = 5
print("Initial c ->", c)

c += 2
print("c += 2 ->", c)

c -= 2
print("c -= 2 ->", c)

c *= 2
print("c *= 2 ->", c)

c /= 2
print("c /= 2 ->", c)

c //= 2
print("c //= 2 ->", c)

c %= 2
print("c %= 2 ->", c)

c **= 2
print("c **= 2 ->", c)
print()


print("----- Membership Operators -----")
list_data = [1, 2, 3, 4, 5]

print("2 in list_data ->", 2 in list_data)
print("10 not in list_data ->", 10 not in list_data)
print()


print("----- Identity Operators -----")
m = [1, 2, 3]
n = [1, 2, 3]
o = m

print("m is n ->", m is n)
print("m is o ->", m is o)
print("m is not n ->", m is not n)
print()