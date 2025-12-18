import random

def snake_water_gun():
    print("Choices: \n-1 for Snake\n0 for Water\n1 for Gun")
    
    user = int(input("Enter your choice (-1 / 0 / 1): "))
    comp = random.choice([-1, 0, 1])
    
    print(f"Computer chose: {comp}")
    
    if user == comp:
        print("It's a draw!")
    elif (user == -1 and comp == 0) or (user == 0 and comp == 1) or (user == 1 and comp == -1):
        print("You win!")
    else:
        print("Computer wins!")

# Call the function
snake_water_gun()
