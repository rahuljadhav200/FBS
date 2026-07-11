#Q4. Write a program to enter P, T, R and calculate the simple interest.
P=int(input("Enter Principle:"))
T=int(input("Enter Time Period:"))
R=float(input("Enter Rate of Interest:"))

SI=(P*T*R)/100
print("Simple Interest is:",SI)