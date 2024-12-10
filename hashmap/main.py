from specialdict import SpecialDict
a=SpecialDict()
a["(2,   3)"]=1
a["(1, 1)"]=2
a["(2)"]=3
a["(3,1,4)"]=3
print(a.ploc(">0"))

