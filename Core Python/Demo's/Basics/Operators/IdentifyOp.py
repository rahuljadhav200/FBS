x=10
y=10
z=20
li1=[10,20]
li2=[10,20]

# 1. is
print(x is y)
print(id(x))
print(id(y))
print(id(z))
print(id(li1))
print(id(li2))
print(y is z)
print(li1 is li2)
print(x is y)


#2. is not 
print(x is not z)
print(li1 is not z)