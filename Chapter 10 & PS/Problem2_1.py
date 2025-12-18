class calculator:
    def __init__(self,n):
        self.n = n
    def square(self):
        print(f"The square of {self.n} is {self.n*self.n}")
    def cube(self):
        print(f"The cube of {self.n} is {self.n*self.n*self.n}")
    def sqrt(self):
        print(f"The sqrt of {self.n} is {self.n ** 0.5}")


num = int(input("Enter the number: "))

# Create object
calc = calculator(num)

# Call methods
calc.square()
calc.cube()
calc.sqrt()