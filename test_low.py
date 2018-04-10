from biba import BIBA

mode="low"

a = BIBA(2,"aaa",mode)
b = BIBA(1,"bbb",mode)
c = BIBA(4,"ccc",mode)
d = BIBA(3,"ddd",mode)
print(a.integrity)
a.read(b)
print(a.integrity)