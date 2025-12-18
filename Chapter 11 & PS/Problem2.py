class Animals:
    pass 

class Pets(Animals):
    pass 

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bhowwwwww Bhow")

d = Dog()
d.bark()
