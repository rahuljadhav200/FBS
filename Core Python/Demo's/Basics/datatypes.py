#Data Types in Python

#-----Numeric-----

#1. Integer
var=10
print(type(var))

#2. Float
var=10.33
print(type(var))

#3. Complex
var=10+5j
print(type(var))
print(var)


#------Text-----

#1. String
var='Firstbit Solutions'
var="Firstbit Solutions"
var='''This is first line.
    This is second line.'''
var="""This is first line.
     This is second line."""
print(type(var))


#----Sequential-----

#1. List
var=[1,2,3,4,5]

#2. Tuple
var=(1,2,3,4,5)
var=1,2,3,4,5

#3. Range
var=range(1,6)
print(type(var))


#----Set Types-----

#1. Set
var={1,2,3,4,5}
print(type(var))

#2. Frozenset
var=frozenset([1,2,3,4,5])
print(type(var))


#----Mapping Types-----

#1. Dictionary
var={"ID":1,"Name":"Rahul Jadhav","Age":25}
print(type(var))


#---Other----

#1. Boolean
var=True
print(type(var))


#--NoneType---
var=None
print(type(var))
