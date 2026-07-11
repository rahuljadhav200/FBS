# WAP a program to swap two numbers using third variable

num1=int(input("Enter the num 1:"))
num2=int(input("Enter the num 2:"))
print(f'Number before swapping num1= {num1} , num2= {num2}')
temp=num1
num1=num2
num2=temp
print(f'Number after swapping num1= {num1} , num2= {num2}')