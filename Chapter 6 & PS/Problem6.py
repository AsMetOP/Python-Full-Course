subject1 = int(input("Enter your marks :"))

subject2 = int(input("Enter your marks :"))

subject3 = int(input("Enter your marks :"))

subject4 = int(input("Enter your marks :"))

subject5 = int(input("Enter your marks :"))

subject6 = int(input("Enter your marks :"))

#total percentage
total_percentage = ((subject1+subject2+subject3+subject4+subject5+subject6)*100)/600

if(total_percentage>90 and total_percentage<=100):
    print("Grade : E","Your Percentage is : ",total_percentage)
    
elif(total_percentage>80 and total_percentage<=90):
    print("Grade : A","Your Percentage is : ",total_percentage)
    
elif(total_percentage>70 and total_percentage<=80):
    print("Grade : B","Your Percentage is : ",total_percentage)
    
elif(total_percentage>60 and total_percentage<=70):
    print("Grade : C","Your Percentage is : ",total_percentage)
    
elif(total_percentage>50 and total_percentage<=60):
    print("Grade : D","Your Percentage is : ",total_percentage)
    
elif(total_percentage<50):
    print("Grade : F","Your Percentage is : ",total_percentage)

else: 
    print("Invalid Input")