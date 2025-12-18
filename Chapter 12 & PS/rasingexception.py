a = int(input("Enter the number: "))
b = int(input("Enter the number: "))

if(b == 0):
    raise ZeroDivisonError("Hey MaaChudaa")
else: 
    print(f"The divison of {a}/{b} is : {a/b}")