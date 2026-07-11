#Q.5 Write a program to enter P, T, R and calculate Compound Interest
P=int(input("Enter Principle:"))
T=int(input("Enter Time Period:"))
R=float(input("Enter Rate of Interest:"))

A=P*(1+R/100)**T
CI= A-P
print("Compound Interest is:",CI)