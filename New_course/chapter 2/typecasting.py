# Type Casting in Python

print("----- Integer Type Casting -----")
a = "10"
b = 3.5
c = True

print("int(a) ->", int(a))
print("int(b) ->", int(b))
print("int(c) ->", int(c))
print()


print("----- Float Type Casting -----")
a = "10"
b = 3
c = True

print("float(a) ->", float(a))
print("float(b) ->", float(b))
print("float(c) ->", float(c))
print()


print("----- String Type Casting -----")
a = 10
b = 3.14
c = True
d = None

print("str(a) ->", str(a))
print("str(b) ->", str(b))
print("str(c) ->", str(c))
print("str(d) ->", str(d))
print()


print("----- Boolean Type Casting -----")
a = 0
b = 1
c = ""
d = "mahi"
e = []
f = [1, 2, 3]

print("bool(a) ->", bool(a))
print("bool(b) ->", bool(b))
print("bool(c) ->", bool(c))
print("bool(d) ->", bool(d))
print("bool(e) ->", bool(e))
print("bool(f) ->", bool(f))
print()


print("----- List Type Casting -----")
a = (1, 2, 3)
b = "abc"

print("list(a) ->", list(a))
print("list(b) ->", list(b))
print()


print("----- Tuple Type Casting -----")
a = [1, 2, 3]
b = "abc"

print("tuple(a) ->", tuple(a))
print("tuple(b) ->", tuple(b))
print()


print("----- Set Type Casting -----")
a = [1, 2, 2, 3]
b = "aabbcc"

print("set(a) ->", set(a))
print("set(b) ->", set(b))
print()


print("----- Dictionary Type Casting -----")
a = [("name", "mahi"), ("age", 25)]

print("dict(a) ->", dict(a))
print()