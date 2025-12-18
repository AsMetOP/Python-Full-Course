# # Without walrus
# data = input("Enter something: ")
# while data != "quit":
#     print("You entered:", data)
#     # data = input("Enter something: ")

# With walrus
while (data := input("Enter something: ")) != "quit":
    print("You entered:", data)

# # Without walrus
# name = input("Enter your name: ")
# if name != "":
#     print(f"Hello, {name}")
# else:
#     print("you entered nothing")

# # With walrus
if (name := input("Enter your name: ")) != "":
    print(f"Hello, {name}")

