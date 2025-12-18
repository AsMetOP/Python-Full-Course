username  = input("Enter you username:")

if(len(username)>10):
    print("Congracts! username is applicable")

elif(len(username)<10):
    print("Your username contains less than 10 characters add more")

else: 
    print("Invalid Username")