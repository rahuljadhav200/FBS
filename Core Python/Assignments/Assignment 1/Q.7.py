#Q.7 Programs to find the roots of a quadratic equations

a=int(input("Enter the Coefficient of x2(Quadratic Coefficient):"))
b=int(input("Enter the Coefficient of x(Linear Coefficient):"))
c=int(input("Enter the Constant term :"))

#Descriminant
d=(b*b)-(4*a*c)
root1=(-b+d**0.5)/(2*a)
root2=(-b-d**0.5)/(2*a)

print("Roots of Quadratic Equation \n Root 1:",root1,'\n Root2:',root2)
