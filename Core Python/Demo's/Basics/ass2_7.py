#Find the sum of three digit number
num=379
#temp = to store the original number
d1=num%10
num=num//10
print(d1)

d2=num%10
num=num//10
print(d2)

d3=num%10
num=num//10
print(d3)

sum=d1+d2+d3
print(f'Sum of three digit number is: {sum}')