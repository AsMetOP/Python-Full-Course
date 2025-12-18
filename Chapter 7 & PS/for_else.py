l = [1,7,8]

for item in l:
    print(item)

else: 
    print("DONE") #this is pointed when loop exhausts

print(".............................")
for j in range(0,81):
    print(j)
    if j==3:     #0,1,2,3
        break

print(".............................")
for i in range(100):
    if(i ==34):
        break
    print(i) #Prints 1-33


print(".............................")
for i in range(100):
    if(i ==34):
        continue
    print(i) #Prints 0-33,35-99


#Pass Statement --> it is a NULL statement is python. Does Nothing