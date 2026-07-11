# Write a program to reverse three digit number

num=int(input("Enter 3 digit number to reverse the digit:"))
numm=num
a=num%10
R1=a*100
num=num//10

b=num%10
R2=b*10
num=num//10
R3=num*1
print(f'The {numm} is the 3 digit no and its reverse is :{R1+R2+R3}')