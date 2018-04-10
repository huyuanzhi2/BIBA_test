from biba import BIBA

mode="strict"

a = BIBA(2,"aaa",mode)
b = BIBA(1,"bbb",mode)
c = BIBA(6,"ccc",mode)
d = BIBA(3,"ddd",mode)
b.read(a)
b.read(c)
d.read(c)