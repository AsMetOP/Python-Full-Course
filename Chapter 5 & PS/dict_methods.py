marks = {
    "Harry" : 100, 
    "Shubham" : 56,
    "Rohan" :35 
}

print(marks.items()) 
#dict_items([('Harry', 100), ('Shubham', 56), ('Rohan', 35)])

print(marks.keys()) 
#dict_keys(['Harry', 'Shubham', 'Rohan'])

print(marks.values())
#dict_values([100, 56, 35])

marks.update({"Harry" : 99, "Renuka" : 100})
print(marks)  
#{'Harry': 99, 'Shubham': 56, 'Rohan': 35, 'Renuka': 100}

print(marks.get("Harry")) #99

print(marks.get("Tanvi")) #none


# print(marks["Tanvi"]) #Error

