#Q.1 Write a program to calculate the percentage of students based on mark of any five subjects ?

print("Enter marks for your 5 subjects:")
sub1= int(input("Math :"))
sub2= int(input("Chemistry:"))
sub3= int(input("Physics:"))
sub4= int(input("Bio:"))
sub5= int(input("Science:"))

total= sub1+sub2+sub3+sub4+sub5
per=(total/500)*100
print('YOu have got',per,'Percentage')
