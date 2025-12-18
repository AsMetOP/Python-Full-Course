class calculator:
    @staticmethod
    def square(n):
        return n * n

    @staticmethod
    def cube(n):
        return n * n * n

    @staticmethod
    def sqrt(n):
        return n ** 0.5

n = int(input("Enter the number: "))
print("Square:", calculator.square(n))   
print("Cube:", calculator.cube(n))  
print("Square Root:", calculator.sqrt(n))  
 