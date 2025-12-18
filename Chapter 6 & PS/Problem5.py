list = ["Asmet", "Tanvi", "Rudra", "Shlok", "Aryan", "Chinmay", "Arnav", "Debrup"]

name = str(input("Enter the name (If registered or not):"))

if name in list:
    print("This name is already registered")
    
else:
    list.append(name)
    print("The updated list is", list)
