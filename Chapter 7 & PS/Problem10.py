# n = int(input("Enter the number:"))

# for i in range(1,11):
#     mul_table = n*(11-i)
#     print(mul_table)

table = []
n = int(input("Enter the number:"))
for i in range(1,11):
    mul_table = n*i
    table.append(mul_table) 
    table.sort()   
    table.reverse()
    print(table)
