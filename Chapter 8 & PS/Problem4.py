# def sum(n):
#     i = 0
#     sum=0
#     while(i<=n):
#         sum +=i
#         i+=1
#     return sum

# n = 4
# print(sum(n))

def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)


print(sum(1))

    
