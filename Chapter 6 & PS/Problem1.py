a = int(input("Enter the number A: "))
b = int(input("Enter the number B: "))
c = int(input("Enter the number C: "))
d = int(input("Enter the number D: "))

if(a>b and a>c and a>d):
    print("A is the greatest :",a)

elif(b>a and b>c and b>d):
    print("B is the greatest :",b)

elif(c>a and c>b and c>d):
    print("C is the greatest :",c)

else: 
    print("D is the greatest :",d)