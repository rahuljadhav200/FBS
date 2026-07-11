gender=input('Enter gender (m/f):')
age=int(input('Enter Age:'))

if(gender=='f'):
    if(age>=18):
        print('Girl is eligible for marriage')
    else:
        print('Pahle padhai kar lo ')
        
else:
    if(age>=21):
        print('Boy is eligible for marriage')
    else:
        print('Pahle Kama lo.')
        
        