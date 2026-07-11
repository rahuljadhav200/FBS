#Find the sum of three digit number

num=int(input("Enter the three digit number:"))
numm=num
a=num%10
num=num//10

b=num%10
num=num//10

num=a+b+num
print(f"The sum of three digit number is :{num}")
