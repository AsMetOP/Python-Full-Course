n = int(input("ENTER THE NUMBER:"))

# Check if the number is less than or equal to 1
if n <= 1:
    print("THIS IS NOT A PRIME NUMBER")
else:
    for i in range(2,n):
        if n % i == 0:
            print("THIS IS NOT A PRIME NUMBER")
            break
    else:
        print("THIS IS A PRIME NUMBER")

