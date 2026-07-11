#WAP to calculate the total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic.\
salary=float(input("Enter the salary of employee:"))
DA= (salary*10)/100
TA= (salary*12)/100
HRA= (salary*15)/100
total= salary+(DA+TA+HRA)
print(f'The salary of employee was:{salary} \n after 10% da is:{DA} \n TA 12% is: {TA} \n and HRA 15% is:{HRA} \n and then total salary of employee is:{total} ')
