#WRITE  a program to swap two numbers without using third variable

num1=int(input("Enter the num 1:"))
num2=int(input("Enter the num 2:"))
print(f'Number before swapping num1= {num1} , num2= {num2}')
num1=num1+num2
num2=num1-num2
num1=num1-num2
print(f'Number after swapping num1= {num1} , num2= {num2}')