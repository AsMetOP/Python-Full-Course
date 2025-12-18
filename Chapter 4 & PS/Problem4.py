numbers = []

num1 = int(input("1st Number: "))
numbers.append(num1)
num2 = int(input("2nd Number: "))
numbers.append(num2)
num3 = int(input("3rd Number: "))
numbers.append(num3)
num4 = int(input("4th Number: "))
numbers.append(num4)

print("The numbers you entered are", numbers)
print("Sum of Numbers are : ", sum(numbers))

numbers.reverse()
print(numbers)

numbers.sort()
print(numbers)
