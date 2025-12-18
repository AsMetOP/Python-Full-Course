a = int(input("Enter your age : "))
if(a>18):
    print("You are above the age content")
    print("Good for you")

elif(a<0): 
    print("You are below the age of concent")

elif(a==0): 
    print("0 kyu enter krra chutiye?")

else: 
    print("Invalid Age")


# 1. There can be any number of Elif statements.
# 2. Last else is executed only if all the conditions inside Elifs fail. 