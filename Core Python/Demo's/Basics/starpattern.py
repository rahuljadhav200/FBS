#Star pattern programs in Python
# rows=10
# for i in range(1, rows + 1):
#     print("*"*i)

# rows=5
# for i in range(rows, 0, -1):
#     print("*"* i)
    
# rows=5
# for i in range (rows):
#  print(" " * (rows-i-1)+ "*" * (i+1))

# rows=5
# for i in range(rows):
#     print("*" * rows)

rows=5
#upper part
for i in range(1, rows +1):
    print(''* (rows-i)+ '*' + '' * (2*i-3) + ('*' if i>1 else ''))
    
#lower part
for i in range (rows-1, 0, -1):
    print('' * (rows-1)+ '*' + '' *(2*i-3) +('*' if i>1 else''))